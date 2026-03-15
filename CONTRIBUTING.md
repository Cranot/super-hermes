# Contributing to Super Hermes

## Adding a New Prism

Prisms are standalone `.md` files in `prisms/`. Each prism is a structured analytical program that tells the model HOW to think.

### Template

Create a new file `prisms/your_prism_name.md`:

```yaml
---
name: your_prism_name
description: "One-line description of what this prism finds"
quality_baseline: null
optimal_model: sonnet
type: structural
---
```

Then write the prism instructions below the frontmatter. Guidelines:
- Use imperative verbs ("Identify...", "Construct...", "Derive...")
- Force construction (build something, then diagnose what it reveals)
- End with concrete outputs (findings table, conservation law)
- Target 50-300 words (compression matters — every word should activate a reasoning operation)
- Test on at least 2 different code files before submitting

### Validation

Before submitting a PR:
1. Run your prism on both included targets: `examples/circuit_breaker.py` and `examples/rate_limiter.py`
2. Compare output quality to an existing prism (e.g., `prisms/l12.md`)
3. Score using the rubric: 10 = conservation law + meta-law + 15+ bugs, 9 = conservation law + bugs, 8 = multiple bugs + structural pattern, 7 = real issues + reasoning

Only prisms scoring 8+ will be merged.

## Adding a New Skill

Skills are `SKILL.md` files in `skills/<skill-name>/`. They follow the [Hermes Agent skill format](https://github.com/NousResearch/hermes-agent).

Required YAML frontmatter: `name`, `description`

## Reporting Issues

Open a GitHub issue with:
- What you ran (skill name, model, file analyzed)
- What you expected
- What you got (paste the output)

## Code of Conduct

Be constructive. The project values intellectual honesty — if something doesn't work, say so clearly.
