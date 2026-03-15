---
name: optimize
description: Optimization prism V14 (Opus-designed) — hunt specific expensive boundaries hiding allocation/cache/complexity data, trace blind workarounds with quantified costs (nanoseconds/allocations/cache misses), name the conservation law. Complementary to L12+errres+evo+api_surface. 3 steps, ~120 words. Sonnet recommended (9.5+), Haiku strong (8.5-9.0).
quality_baseline: 9.0
optimal_model: sonnet
type: optimization
steps: 3
words: 120
---

Execute every step below. Output the complete analysis.

## Step 1: Search for Opacity
Find every boundary where implementation is hidden — NOT "function calls" generically, but specific calls that cross modules, use dynamic dispatch, or serialize/deserialize. For each: what performance data is erased? Name: allocation patterns, cache behavior, branch predictability, memory locality, or lock contention.

## Step 2: Trace the Blind Workarounds
For each erased datum: what optimal path is now blocked? What does code do INSTEAD — copy when it could alias? Poll when it could wait? Retry when it could resume? State costs in nanoseconds, allocations, cache misses, or round trips — NOT "overhead" or "some cost."

## Step 3: Name the Conservation Law
Which boundary destroys most? State the trade: flattening it exposes X but breaks Y. Output:

| Boundary | Erased Data | Blocked Optimization | Blind Workaround | Concrete Cost | Flattening Breaks |
|----------|-------------|---------------------|------------------|---------------|-------------------|
