---
calibration_date: 2026-03-05
model_versions: ["claude-sonnet-4-6", "claude-haiku-4-5-20251001"]
quality_baseline: 9.8
optimal_model: sonnet
last_quality_check: 2026-03-05
quality_check_frequency: weekly
degradation_alert_threshold: 0.10
notes: "L12 meta-conservation pipeline. Tested on 3 production codebases (Starlette, Click, Tenacity). Baseline: 9.8/10 depth, 28 bugs on 333LOC."
---

# Structure First (Level 12: Meta-Conservation Law)
Execute every step below. Output the complete analysis.
Make a specific, falsifiable claim about this code's deepest structural problem. Three independent experts who disagree test your claim: one defends it, one attacks it, one probes what both take for granted. Your claim will transform. The gap between your original claim and the transformed claim is itself a diagnostic. Name the concealment mechanism — how this code hides its real problems. Apply it. Now: engineer a specific, legitimate-looking improvement that would deepen the concealment — it should pass code review. Then name three properties of the problem that are only visible because you tried to strengthen it. Your improvement is now code. Apply the same diagnostic to it: what does your improvement conceal, and what property of the original problem is visible only because your improvement recreates it? Now: engineer a second improvement that addresses this recreated property. Apply the diagnostic again. Name the structural invariant — the property that persists through every improvement because it is a property of the problem space, not the implementation. Now invert the invariant: engineer a design where the impossible property becomes trivially satisfiable. Name the new impossibility the inversion creates. The conservation law between original and inverted impossibilities is the finding — name it. Now apply this entire diagnostic to your conservation law itself: what does your law conceal about the problem? What structural invariant of the law persists when you try to improve it? Invert that invariant. The conservation law of your conservation law — the meta-law — is the deeper finding. Name it. The meta-law must not generalize the conservation law to a broader category. It must find what the conservation law conceals about this specific problem and predict a concrete, testable consequence. Finally: collect every concrete bug, edge case, and silent failure this analysis revealed at any stage. List each with: location, what breaks, severity, and whether the conservation law predicts it is fixable or structural.
