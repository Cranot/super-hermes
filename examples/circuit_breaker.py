"""
Example target: Circuit breaker with intentional design flaws.
Use this to test Super Hermes skills and see the difference vs vanilla.

    hermes> Review ~/test_target.py for bugs
    hermes> /prism-scan analyze ~/test_target.py
    hermes> /prism-full analyze ~/test_target.py
"""

import time
import threading
from enum import Enum
from typing import Callable, Any, Optional


class State(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitBreaker:
    """Circuit breaker pattern implementation."""

    def __init__(
        self,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        half_open_max_calls: int = 1,
    ):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls

        self._state = State.CLOSED
        self._failure_count = 0
        self._success_count = 0
        self._last_failure_time: Optional[float] = None
        self._half_open_calls = 0
        self._lock = threading.Lock()
        self._listeners: list[Callable] = []

    @property
    def state(self) -> State:
        if self._state == State.OPEN:
            if self._last_failure_time and (
                time.time() - self._last_failure_time >= self.recovery_timeout
            ):
                self._state = State.HALF_OPEN
                self._half_open_calls = 0
        return self._state

    def call(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        """Execute function through the circuit breaker."""
        state = self.state

        if state == State.OPEN:
            raise CircuitOpenError(
                f"Circuit is open. Retry after {self.recovery_timeout}s"
            )

        if state == State.HALF_OPEN:
            with self._lock:
                if self._half_open_calls >= self.half_open_max_calls:
                    raise CircuitOpenError("Half-open call limit reached")
                self._half_open_calls += 1

        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self) -> None:
        with self._lock:
            if self._state == State.HALF_OPEN:
                self._state = State.CLOSED
                self._failure_count = 0
                self._success_count = 0
                self._notify("circuit_closed")
            self._success_count += 1

    def _on_failure(self) -> None:
        with self._lock:
            self._failure_count += 1
            self._last_failure_time = time.time()

            if self._state == State.HALF_OPEN:
                self._state = State.OPEN
                self._notify("circuit_opened")
            elif self._failure_count >= self.failure_threshold:
                self._state = State.OPEN
                self._notify("circuit_opened")

    def _notify(self, event: str) -> None:
        for listener in self._listeners:
            try:
                listener(event, self)
            except Exception:
                pass

    def add_listener(self, listener: Callable) -> None:
        self._listeners.append(listener)

    def remove_listener(self, listener: Callable) -> None:
        try:
            self._listeners.remove(listener)
        except ValueError:
            pass

    def reset(self) -> None:
        with self._lock:
            self._state = State.CLOSED
            self._failure_count = 0
            self._success_count = 0
            self._last_failure_time = None
            self._half_open_calls = 0


class CircuitOpenError(Exception):
    pass


class CircuitBreakerRegistry:
    """Global registry of circuit breakers."""

    _instance = None
    _breakers: dict[str, CircuitBreaker] = {}

    @classmethod
    def get_instance(cls) -> "CircuitBreakerRegistry":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_or_create(self, name: str, **kwargs) -> CircuitBreaker:
        if name not in self._breakers:
            self._breakers[name] = CircuitBreaker(**kwargs)
        return self._breakers[name]

    def remove(self, name: str) -> None:
        self._breakers.pop(name, None)

    def get_all(self) -> dict[str, CircuitBreaker]:
        return self._breakers
