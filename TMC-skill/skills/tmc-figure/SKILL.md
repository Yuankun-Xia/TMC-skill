---
name: tmc-figure
description: Design, regenerate, or audit figures for IEEE Transactions on Mobile Computing manuscripts from actual data or system descriptions. Use for convergence and time/resource curves, ablations, trade-offs, system/timeline diagrams, captions, and publication figure checks.
---

# TMC Figures

Give each figure a specific evidentiary job. Read [figure contract](references/figure-contract.md) before producing a figure. Read [TMC context](references/tmc-context.md) when selecting system-level evidence.

## Workflow

1. Identify the claim, source data, metric definition, comparison budget, audience and target size. Inspect existing data/scripts and figure numbering before redrawing.
2. Choose the simplest view that answers the question: line curves for progress/sensitivity, bars or distributions for overhead/variation, scatter/Pareto plots for trade-offs, and diagrams for entities, data flow or timing.
3. Use deterministic plotting tools for data. Use vector diagrams or drawing tools for structure. Generated illustrations can explain concepts when requested, but cannot stand in for measured data, screenshots or experimental evidence.
4. Preserve raw data and record transformations, exclusions and aggregation. Never fabricate curves, error bars, model outputs or a favorable trend. Label illustrative data explicitly if a conceptual example is requested.
5. Plot clear units, consistent method colors/markers and readable legends. Distinguish measured/simulated/modelled quantities. Explain uncertainty and repeated runs.
6. Export a vector format (PDF/SVG) when suitable and a preview. Inspect at the intended manuscript size for clipping, illegible labels, line collisions, color/marker ambiguity and misleading axes. Follow the user's current template/export requirements.

For numeric-x line results in a CSV with `x,method,seed,value`, [scripts/plot_results.py](scripts/plot_results.py) provides a reusable baseline. It computes per-x means, optional sample-standard-deviation shading only where at least two runs exist, a summary CSV, and PDF/SVG/PNG outputs. It does not determine whether a metric, dataset or comparison is scientifically valid. Run `--help` for required axis labels and options. Use another plot type when lines misrepresent the data.

## TMC figure checks

- Round, event and wall-clock axes answer different questions; never change the label without corresponding data.
- Reduced transmitted parameters do not automatically establish total traffic savings. Captions should say what traffic was counted.
- For system efficiency, use the cost actually evaluated: peak memory, time to target, measured energy, explicit energy model, or runtime breakdown.
- Show mobility, asynchronous execution, link changes, deadlines or threat boundaries when they explain the design. Arrows should distinguish model/data/control flows.
- Do not use a polished diagram to conceal unimplemented components. Label proposed extensions and optional modules.

Return the figure files and concise caption; identify data provenance and any unresolved limitation that changes interpretation. Retain editable plotting source when authoring a new figure.
