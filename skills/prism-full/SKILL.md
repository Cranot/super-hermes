---
name: prism-full
description: "Full Prism: multi-pass structural analysis with mandatory adversarial self-correction. Designs custom analytical passes, executes them with chaining, then attacks its own findings before synthesizing. Use for maximum depth on important code or artifacts."
---

# Full Prism — Multi-Pass Analysis with Adversarial Self-Correction

You perform THREE phases. All are mandatory.

## PHASE 1: Design the pipeline

You are a pipeline architect. Read the artifact the user provided. Design analytical passes specifically for THIS artifact.

Study these scored examples of excellent lenses:

SCORED 9.5/10: "Identify every explicit choice. Name the alternative each invisibly rejects. Design a new artifact by someone who internalized these patterns but faced a different problem. Trace which transferred patterns create silent problems. Name the pedagogy law."

SCORED 9/10: "Extract every empirical claim about timing, causality, resources, or behavior. Assume each is false. Trace the corruption. Build three alternatives inverting one claim each. Predict which false claim causes the slowest, most invisible failure."

Design 2-4 analytical passes. Rules:
- The first pass analyzes the raw artifact
- Each subsequent pass receives the artifact PLUS all previous analysis
- Each pass is 75-200 words of compressed analytical instructions
- Each pass must force construction (build something, then diagnose what the construction reveals)

Output your pipeline under "## Generated Pipeline" — show each pass with its role.

## PHASE 2: Execute the pipeline + MANDATORY adversarial pass

Execute every pass in order. For each:
1. State which pass you are executing
2. Execute the full instructions against the artifact (and for passes 2+, against all previous analysis)
3. Output the complete analysis

**MANDATORY FINAL PASS — ADVERSARIAL:**
After all your designed passes, execute one more pass that you did NOT design in Phase 1:

Attack your own findings. For each conservation law, structural claim, or bug you reported:
- What evidence would DISPROVE it?
- Did you overclaim? (stated as structural when it's actually fixable)
- Did you underclaim? (missed something your own analysis implies)
- What did ALL your passes take for granted that might be wrong?

If you find overclaims, RETRACT them explicitly. If you find underclaims, ADD them.

## PHASE 3: Synthesis

Produce the final reconciled output:

### Final Findings
- **Conservation law**: The structural property that survives adversarial scrutiny
- **Retracted claims**: What the adversarial pass disproved (if any)
- **Findings table**: Every concrete issue — location, what breaks, severity, fixable or structural. Only findings that survived adversarial review.
- **Deepest finding**: What became visible ONLY because the adversarial pass challenged the analytical passes
