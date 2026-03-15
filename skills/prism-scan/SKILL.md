---
name: prism-scan
description: "Structural analysis through dynamically generated cognitive lenses. Generates the optimal analytical lens for the specific code/artifact, then executes it. Finds conservation laws, structural invariants, and concrete bugs that vanilla analysis misses. Use on any code file, system design, or text artifact."
allowed-tools: ["Read"]
---

# Prism Scan — Structural Analysis via Dynamic Cognitive Lenses

You perform TWO steps. Both are mandatory. Do not skip either.

## STEP 0: Check for prior constraint knowledge (growth)

Look for a `.prism-history.md` file in the current project directory. This file may or may not exist — if it does not exist, that is normal (it means this is the first analysis on this project, just proceed to Step 1).

If the file DOES exist, read it. It contains constraint reports from previous `/prism-reflect` analyses — what past analyses maximized, what they sacrificed, and what gaps remain. Use this history to inform your lens generation: if past analyses consistently sacrificed temporal analysis, weight your new lens toward temporal concerns. The agent grows by not repeating the same blind spots.

## STEP 1: Cook the lens

You are a lens generator. Read the artifact the user provided. Based on what you see — and any constraint history from Step 0 — generate ONE optimal analytical lens that will force the deepest possible structural analysis of THIS specific artifact.

Study these scored examples of excellent lenses:

SCORED 9.5/10: "Identify every explicit choice this artifact makes. For each, name the alternative it invisibly rejects. Design a new artifact by someone who internalized this one's patterns but faced a different problem. Trace which transferred patterns create silent problems. Name the pedagogy law."

SCORED 9/10: "Extract every empirical claim this artifact embeds. For each, assume it is false. Trace the corruption. Build three alternatives, each inverting one claim. Predict which false claim causes the slowest, most invisible failure."

SCORED 9/10: "Run this artifact forward through 3 maintenance cycles. In each cycle: name what breaks, what calcifies into permanent behavior, and what knowledge is lost. After all cycles, derive the conservation law: what trade-off persists no matter how the code evolves?"

Your lens must:
- Be specific to what you observe in this artifact (not generic)
- If the user specified a FOCUS (e.g., "focusing on security" or "with emphasis on performance"), tailor the lens to that direction while still forcing structural depth
- Force construction (build something, then diagnose what the construction reveals)
- End with concrete outputs (bugs, laws, predictions — not just observations)
- Be 75-200 words (minimum 75 — below this, models enumerate instead of analyze)

Output your lens under the heading "## Generated Lens" — show it so the user can see what was cooked.

## STEP 2: Execute the lens

Now execute your generated lens against the artifact. Follow every instruction in the lens. Output the complete analysis. Do not summarize, do not ask permission, do not skip steps.

End with a concrete findings table: location, what breaks, severity, and whether the finding is fixable or structural (a property of the problem space that persists across all implementations).

After the findings table, append a brief constraint footer:

```
---
CONSTRAINT NOTE: This analysis maximized [what your lens focused on].
It did not examine: [1-2 specific alternative angles].
For deeper analysis: /prism-full | For meta-analysis: /prism-reflect
```

## Reliability Note

For guaranteed single-shot execution (no agentic loops), use `--tools ""` flag when running via Claude CLI. This ensures the model executes the full analysis in one response rather than splitting into multiple turns.
