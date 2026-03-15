---
name: error_resilience
description: Error resilience prism V11 (Sonnet-designed) — search for every failure silence including implicit boundaries (coercions, defaults, null checks), trace multi-hop wrong decisions to user-visible harm, engineer opposing fixes to discover invariant. Complementary to L12+optim+evo+api_surface. 3 steps, ~165 words. Sonnet recommended (9.0+), Haiku strong (8.7-9.0).
quality_baseline: 10.0
optimal_model: sonnet
type: error_resilience
steps: 3
words: 165
---

Execute every step below. Output the complete analysis.

## Step 1: The Error Boundaries
Search for every catch, wrap, transform, OR silence of a failure. Include implicit boundaries: coercions swallowing mismatches, defaults masking undefined, callbacks never firing, null checks skipping work. For each: what specific failure context (variable values, stack depth, partial state, timing) is preserved vs destroyed? NOT "the message" — name exact fields and state lost.

## Step 2: The Missing Context
For each destroyed datum: trace forward through ALL downstream code. What decision branch needs it to choose correctly? What WRONG branch is taken instead? Follow the wrong branch until it (a) raises a misleading error with wrong diagnosis, or (b) returns an incorrect result silently. NOT single-hop — trace through function calls and conditionals to user-visible harm.

## Step 3: The Impossible Fix
Pick the boundary destroying the MOST information. Engineer minimal fix to preserve it. What NEW information does your fix destroy? Now engineer the OPPOSITE fix — preserve what the first destroyed, destroy what the first preserved. What survives both? Name the structural invariant. Output: | Boundary | Destroyed | Wrong Decision | Harm | Fix A Destroys | Fix B Destroys | Invariant |.
