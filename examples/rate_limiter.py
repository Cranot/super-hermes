# Example target for prism validation. Has intentional concurrency and timing bugs.

import time
import threading


class TokenBucketRateLimiter:
    """Simple token bucket rate limiter.

    Allows up to `capacity` requests, refilling at `refill_rate` tokens/second.
    """

    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()
        self._lock = threading.Lock()

    def _refill(self):
        """Add tokens based on elapsed time since last refill."""
        now = time.time()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.refill_rate
        # BUG: no overflow protection — tokens can exceed capacity
        self.tokens += new_tokens
        self.last_refill = now

    def allow(self) -> bool:
        """Check if a request is allowed. Consumes one token if so."""
        self._refill()
        # BUG: race condition — _refill() and token check/decrement
        # are not atomic; another thread can interleave between them
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

    def wait(self, timeout: float = 10.0) -> bool:
        """Block until a token is available or timeout expires."""
        # BUG: time.time() called at start but not rechecked consistently
        # in the loop — elapsed calculation drifts under heavy load
        deadline = time.time() + timeout
        while True:
            if self.allow():
                return True
            remaining = deadline - time.time()
            if remaining <= 0:
                return False
            # Sleep a fraction of the time until next token
            sleep_time = 1.0 / self.refill_rate
            time.sleep(min(sleep_time, remaining))

    def get_tokens(self) -> float:
        """Return current token count (approximate under concurrency)."""
        return self.tokens

    @property
    def is_throttled(self) -> bool:
        """True if no tokens are currently available."""
        # BUG: calls _refill() which mutates state — property has
        # write side effect, same read as allow() but doesn't consume
        self._refill()
        return self.tokens < 1
