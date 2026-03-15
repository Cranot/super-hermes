---
name: simulation
description: Temporal simulation prism — run forward through maintenance cycles to find what calcifies, what knowledge is lost, and what becomes unfixable. Finds temporal fragility invisible to static analysis. 5 cycles + conservation law + diagnostic. ~170 words. Sonnet recommended (9.0+), Haiku strong (8.5).
quality_baseline: 9.0
optimal_model: sonnet
type: simulation
steps: 5
words: 170
origin: "Round 39 alternative primitives (hand-crafted)"
---

Execute every step below. Output the complete analysis.

## Temporal Simulation Protocol

Run this code forward through five maintenance cycles. For each cycle, name what breaks, what calcifies, and what knowledge is lost.

**Cycle 1**: A new developer joins. They must add a feature. What do they misunderstand about this code? Which assumption will they violate? What breaks?

**Cycle 2**: A dependency updates with breaking changes. Which interfaces absorb the shock? Which propagate it? What emergency patches will calcify into permanent code?

**Cycle 3**: The original author leaves. What undocumented knowledge is now lost? Which design decisions become cargo cult? What becomes unfixable?

**Cycle 4**: Usage grows 10x. What performance assumptions fail? Which "temporary" solutions become permanent load-bearing infrastructure?

**Cycle 5**: A security audit occurs. What hidden trust assumptions are exposed? Which boundaries were never boundaries?

## Derive

Map the calcification pattern. What quantity is conserved across all five cycles? Name the conservation law: A × B = constant. What did the code sacrifice?

## Diagnostic

Apply this law to your own simulation. What temporal assumption does YOUR analysis make? What would a sixth cycle reveal about your predictions?
