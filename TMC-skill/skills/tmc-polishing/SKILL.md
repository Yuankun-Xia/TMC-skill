---
name: tmc-polishing
description: Polish or translate existing IEEE Transactions on Mobile Computing manuscript prose into clear technical English while preserving claims, equations, measurements, and evidence strength. Use for TMC paragraph editing, academic English, Chinese-to-English revision, and concision; use tmc-writing when the manuscript argument or section must be built.
---

# TMC Technical Polishing

Improve existing prose at the level the user requests. Accept Chinese notes and explain substantive choices in Chinese when useful. Default to English manuscript prose unless the user explicitly requests another manuscript language; Chinese notes or chat alone do not change that default.

Read [technical meaning and editing patterns](references/technical-meaning.md) for terminology, quantitative language, and scientific ambiguity. Read [TMC context](references/tmc-context.md) for venue-related edits. Neither journal scope nor this corpus dictates a fixed sentence length, section order, or mandatory theorem/testbed.

## Editing workflow

1. Identify the section's purpose, scope of editing, and technical claims already present. Preserve LaTeX labels, citation keys, commands, math, and notation unless the requested correction requires a change.
2. Distinguish language problems from missing scientific information. Repair grammar, reference ambiguity, and paragraph order where meaning is established. Flag unsupported inferences instead of hiding them with fluent prose.
3. Preserve the operational definitions and evidence strength: convergence in rounds versus elapsed time; resource proxies versus measured resources; observed robustness versus guarantees.
4. Make logical relations explicit. Prefer concrete subjects and verbs; define unfamiliar acronyms. Keep terminology stable across the excerpt and maintain the author's legitimate technical style.
5. Compare the revision to the source for changed numbers, units, comparisons, uncertainty, assumptions, causality, novelty, scope, and negative results.

For substantial restructuring, explain the changed argument order. For light polishing, do not silently redesign the research story. When meaning cannot be recovered, mark the ambiguity and offer a bounded alternative; do not guess an experiment, theorem, or mechanism.

## Output

Lead with the polished text. Add a few Chinese notes only for material choices or missing information. Provide a before/after table when requested. Do not generate a full manuscript audit for a single sentence.

For a LaTeX edit, preserve compilable source and make local changes. Confirm compilation only if a compiler actually succeeded. For Word tracked changes or PDF layout work, use available format-specific tools and check the rendered result when needed.
