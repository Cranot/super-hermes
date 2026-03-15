# Super Hermes

**The agent that knows what it can't do.**

Super Hermes teaches Hermes Agent to write its own thinking instructions, report what it found AND what it missed, and grow smarter with every analysis.

**Vanilla Hermes:** "The session handling is tightly coupled. Consider decoupling."
*Names a pattern. Tells you what to change.*

**Super Hermes:** "Session state is non-monotonic. No append-only, composable, or lazy architecture can manage it without sacrificing consistency or isolation. **This is a structural impossibility, not a code flaw.**"
*Derives WHY the code must be this way. Tells you what you can't change — and what to do instead.*

**Plus a constraint report:** "This analysis maximized structural depth. It did not examine temporal degradation or security surfaces. For those: `/prism-reflect`"

The difference isn't intelligence — it's cognitive structure:

| | Vanilla (same model, same code) | With prism |
|---|---|---|
| Output | 339 words | 1,485 words |
| Finds bugs | 7 (surface checklist) | 11 (with line refs, severity, structural classification) |
| Finds structural trade-offs | No | Yes — conservation law derived |
| Reports blind spots | No | Yes — constraint footer |
| Cost | ~$0.05 | ~$0.05 (same) |

*Validated on real open-source codebases: Starlette routing.py (333 lines), Click core.py (417 lines), Tenacity retry.py (331 lines). Full outputs in `examples/`.*

*Every bug in the examples has exact line numbers you can verify. The race condition in `circuit_breaker.py` (impure `state` property writing `_state` without lock) is independently reproducible — inspect the code yourself.*

---

## What It Does

Before any complex task, Super Hermes **writes its own thinking instructions** — a cognitive prism tailored to the specific problem. Different problems get different prisms. Then it executes the prism and reports both what it found AND what it couldn't see.

**Example:** Given a circuit breaker implementation, the agent generated:

> *"Identify every temporal assumption in this artifact's state transitions. Simulate concurrent execution that violates each. Construct three alternatives inverting one temporal assumption each. Trace which creates silent statistical failures rather than immediate exceptions."*

The agent wrote that. Then it executed it and found a concurrency trilemma — a structural property that persists across ALL possible implementations.

---

## Skills

| Skill | What it does | Calls |
|---|---|---|
| `/prism-scan` | Generate optimal lens for this artifact, execute it, report findings + constraints. Add "focusing on X" to direct the lens. | 1 |
| `/prism-full` | Multi-pass pipeline with mandatory adversarial self-correction — later passes attack earlier findings | 1 (multi-pass within single response) |
| `/prism-3way` | WHERE/WHEN/WHY — three orthogonal operations + cross-operation synthesis. Works on any domain (code, business, strategy, text). | 1 |
| `/prism-discover` | Map every possible analysis domain for an artifact | 1 |
| `/prism-reflect` | Self-aware analysis — structural findings + meta-analysis of what the analysis concealed + constraint transparency report | 2-3 |

### Proven Prisms (included in `prisms/`)

7 battle-tested analytical lenses from the research. Use directly with Hermes or any tool that supports system prompts:

| Prism | What it finds | Validated score |
|-------|--------------|-----------------|
| `error_resilience.md` | Corruption cascade chains — silent exits, deferred failures, state corruption | 10.0/10 |
| `l12.md` | Conservation laws (structural trade-offs that can't be engineered away — like CAP theorem for your code) + meta-laws + concrete bugs | 9.8/10 |
| `optimize.md` | Critical path tracing — safe fixes (reduce work) vs unsafe (skip work) + conservation law | 9.5/10 |
| `identity.md` | What code claims to be vs what it actually does | 9.5/10 |
| `deep_scan.md` | Information destruction, laundering, silent transformation | 9.0/10 |
| `claim.md` | Assumption inversions — what if accepted truths are false? | 9.0/10 |
| `simulation.md` | Temporal prediction — what breaks over time | 9.0/10 |

*Scores are from AI-evaluated depth across real open-source codebases (Starlette, Click, Tenacity, Flask, Rich, Requests). Raw outputs available in the [research repo](https://github.com/Cranot/agi-in-md).*

These prisms work independently of the skills — use them as system prompts with `claude -p --system-prompt-file prisms/l12.md`, with the Anthropic API, or with any LLM tool. The `/prism-scan` skill generates custom lenses dynamically; these proven prisms are pre-built alternatives with validated quality.

### /prism-3way — Multi-Angle Analysis

Attacks the problem from three orthogonal directions in a single run:
- **WHERE** (archaeology): dig through structural layers — what's visible, what's hidden, what's between
- **WHEN** (simulation): run forward through time — what breaks, calcifies, gets lost
- **WHY** (impossibility): prove which desirable properties can't coexist

Then a **synthesis** cross-references all three — agreements are structural certainties, disagreements are where the real insight hides. Works on code, business plans, strategy docs, research — any domain.

### /prism-reflect — The Differentiator

Most agents tell you what they found. `/prism-reflect` also tells you what it **missed**:

```
CONSTRAINT REPORT
═══════════════════════════════════════════════════

This analysis used: Structural depth pipeline
Maximized: Conservation laws, bug classification, ownership chains
Sacrificed: Temporal prediction, security analysis, user adaptation

Recommendations:
- For how this code degrades over time: /prism-scan with temporal focus
- For security attack surfaces: /prism-scan with security focus
- For full multi-angle coverage: /prism-full

Conservation law of this analysis:
Depth × Breadth = Constant. I went deep on structure.
I went shallow on everything else. Now you know.
═══════════════════════════════════════════════════
```

**Why this matters:** You can't trust an agent that doesn't know its limits. Every analysis has blind spots. `/prism-reflect` makes them visible so you can fill the gaps.

---

## Install

```bash
git clone https://github.com/Cranot/super-hermes.git
cd super-hermes
bash install.sh
```

On Windows: `powershell -ExecutionPolicy Bypass -File install.ps1`

Or manually:
```bash
cp -r skills/* ~/.hermes/skills/
cp -r prisms/ ~/.hermes/prisms/    # proven analytical lenses
```

Requires [Hermes Agent](https://github.com/NousResearch/hermes-agent). Works with any model Hermes supports.

### Try it now (no Hermes needed)

```bash
cat your_code.py | claude -p --system-prompt-file prisms/l12.md --model sonnet --tools ""
```

```bash
# Or test on a real open-source file:
curl -s https://raw.githubusercontent.com/encode/starlette/master/starlette/routing.py | claude -p --system-prompt-file prisms/l12.md --model sonnet --tools ""
```

You should see: a **Generated Lens** (custom analytical instructions), a **findings table** (bugs with line numbers and severity), and a **conservation law** (structural trade-off that can't be engineered away). If you see a generic code review instead, the prism didn't load — check the file path.

The 7 prisms work with any tool that supports system prompts — Claude CLI, Anthropic API, Cursor, or any LLM.

### Try it with Hermes

```
hermes> /prism-scan analyze examples/circuit_breaker.py
```

Real output from Hermes Agent (truncated):

```
⚡ Loading skill: prism-scan

  ┊ 🔎 grep      .prism-history.md  0.7s

No prior constraint history. Analyzing fresh.

## Generated Lens
"Extract the temporal invariant in state transitions. Map every state path
from CLOSED → OPEN → HALF_OPEN → CLOSED. For each transition, identify:
(1) what determines the transition happens, (2) what could block it,
(3) whether the state is mutated inside or outside the critical section.
Build a second circuit breaker that inverts the lock placement..."

## Conservation Law
"Decentralized lock placement in a state machine with time-based transitions
creates a fundamental trade-off: either (1) atomicity is sacrificed, or
(2) lock contention increases because read operations must hold the lock."

CONSTRAINT NOTE: This analysis maximized temporal correctness and lock
placement asymmetry. It did not examine: listener performance/blocking
impact under load, integer overflow on failure_count.
```

*Real output from Hermes Agent (Claude Haiku 4.5 via OpenRouter) on `examples/circuit_breaker.py`. The underlying prism methodology is validated on 6 real open-source codebases in the [research repo](https://github.com/Cranot/agi-in-md). See `examples/` for all skill outputs from a complete Hermes session.*

---

## How It Works Under the Hood

A prism is a structured analytical program — not "analyze this code" but a step-by-step construction protocol. Here's what `prisms/l12.md` (332 words) tells the model to do:

> *Make a falsifiable claim about the deepest problem. Three experts attack it — one defends, one attacks, one probes assumptions. Engineer an improvement that deepens the concealment. Name what the improvement reveals. Engineer a second improvement. Find the structural invariant that persists through every improvement. Invert it. The conservation law between original and inverted impossibilities is the finding. Apply the diagnostic to the law itself. The meta-law is the deeper finding. Collect every concrete bug.*

This is a **program** the model executes. Different code → different construction paths → different findings. The model doesn't "think harder" — it follows a different analytical procedure than vanilla prompting.

The `/prism-scan` skill takes this further: instead of using a fixed prism, it generates a **custom** one for each artifact. The model reads your code, decides what analytical approach fits, writes the instructions, then follows them.

Unlike chain-of-thought (show your reasoning) or tree-of-thought (explore branches), prisms force **construction** — build something, watch it fail, derive what survives. This produces findings that enumeration cannot reach, because the construction reveals properties that were invisible before the attempt.

Based on the [cognitive compression taxonomy](https://github.com/Cranot/agi-in-md): 1,000+ experiments across 40 research rounds, 204+ empirical principles. Validated inside Hermes Agent (Gemini 2.5 Flash). Also proven on Claude Sonnet, Hermes 3 (Llama 405B), and Llama 3.1 70B.

---

## "The Agent That Grows With You"

Other agents grow by accumulating data about you. Super Hermes grows by accumulating **thinking strategies** — learning WHICH analytical approach works for WHICH problem.

**What's built and working:**
- **7 proven prisms** ship in `prisms/` — battle-tested analytical lenses from 1,000+ experiments, ready to use immediately.
- **The cooker** generates NEW prisms on the fly — every problem gets a custom-tailored analytical approach. No two analyses are identical.
- **Constraint history** — `/prism-reflect` saves its constraint report to `.prism-history.md` in your project. The next time `/prism-scan` runs on any file in the same project, it reads past constraint reports and adjusts its lens to cover previously missed angles. The agent literally learns from its own blind spots.
- **Self-governance** — an agent that reports what it can't see enables informed decisions about when to go deeper vs when to accept the analysis.

**The growth loop:**
```
/prism-scan code.py → generates lens, produces analysis + constraint footer
/prism-reflect code.py → deeper analysis + saves constraint report to .prism-history.md
/prism-scan other_file.py → reads .prism-history.md, adjusts lens to cover past gaps
                            ↑ THIS is "grows with you" — the agent gets smarter per project
```

*The growth loop is demonstrated in [`examples/growth-demo.md`](examples/growth-demo.md) — same code, same skill, genuinely different analysis because the agent learned from its previous blind spots. See [Limitations](#limitations) for caveats.*

---

## Limitations

- **Single-file analysis.** Skills analyze one file at a time. Cross-file architectural analysis is not supported yet.
- **Model-dependent quality.** Validated inside Hermes Agent on Gemini 2.5 Flash (full skill loading, tool use, .prism-history.md creation). Also tested on Claude Sonnet (1,485w), Hermes 3 / Llama 405B (439w), and Llama 70B (617w). All follow the skill structure. Sonnet produces the deepest standalone output; Gemini inside Hermes Agent autonomously wrote and executed test scripts.
- **Growth mechanism is minimal.** The `.prism-history.md` feedback loop is an append-only text file — no pruning, no semantic indexing, no validation that adjustments improve subsequent analyses. Future: structured constraint store with semantic deduplication and pruning.
- **No automated benchmarks.** Depth scores (9.8/10, 9.0/10) are from AI-evaluated experiments in the research project, not from standardized external benchmarks. Scoring rubric: 10 = conservation law + meta-law + 15+ bugs with line refs; 9 = conservation law + bugs + structural insight; 8 = multiple concrete bugs + deeper pattern; 7 = real issues + structural reasoning. Evaluated by Claude on real open-source codebases (Starlette, Click, Tenacity, Flask, Rich, Requests).
- **Hermes dependency.** Skills require Hermes Agent. The 7 prisms in `prisms/` work standalone with any system-prompt-capable tool.

---

## The Science

Full research, experiment logs, compression taxonomy, and 33 production prisms: [agi-in-md](https://github.com/Cranot/agi-in-md)

Key findings from the research:
- **40 research rounds**, 1,000+ experiments, 204+ empirical principles
- **Tested on individual files up to 2,700 lines with no quality degradation**
- **Conservation laws are structural** — they persist across all implementations, not just the one analyzed
- **Meta-analysis works** — a second analytical pass genuinely finds what the first pass conceals
- **Cost inversion proven** — structured prompts on cheap models beat expensive models without them

---

## License

MIT
