# Figure contract

Before drawing, establish `claim | data/source | x/y definitions and units | comparison budget | aggregation | intended width`. Use the existing style if the user is revising a paper.

## Match view to question

| Question | View | Frequent error |
|---|---|---|
| How quickly does learning progress? | Accuracy/loss versus rounds, elapsed time, traffic or energy | Claiming speed from rounds when workloads differ |
| Where is cost spent? | Runtime/energy breakdown or grouped bars | Omitting control, idle or communication cost |
| What is the trade-off? | Accuracy versus memory/energy/time, or Pareto scatter | Comparing different targets or joining unordered categories |
| Which component matters? | Ablation bars/curves with matched budgets | Changing model capacity and mechanism simultaneously |
| Does performance vary across clients? | CDF, box/violin plot, per-client distribution | Hiding excluded clients behind a global mean |
| How does the system run? | Architecture, protocol sequence or timeline | Showing flow without message content, timing or decision roles |

A diagram can be schematic without being to scale, but state that where it matters. Keep model/data/control arrows distinct; use labels rather than color alone. Mark the measured system boundary, cloud/edge/client roles, and stale versions for asynchronous protocols when relevant.

## Numerical integrity

Use source arrays/logs, not values estimated from a screenshot, when available. Digitized values need a digitization label and uncertainty; do not report them as original raw measurements. Never alter a curve to match a textual claim.

Compute statistics across independent runs at matched x values. Document how irregular sampling, missing runs, timeouts and failures are handled. Do not interpolate across unobserved intervals by default. Error bars need an identified statistic and n. Report n that changes across x.

For normalized metrics, define the reference and direction. Bar plots normally start at zero; a different choice needs a clear reason and visible axis. Use log scales for a justified dynamic range and reject nonpositive values. Make differing axis scales and broken axes unmistakable. Avoid dual axes that imply unsupported correlation.

## Caption

State what is compared, the operative condition/budget, units if not obvious, n/statistic if applicable, and panel meanings. Distinguish `measured`, `simulation`, `modelled`, and `illustrative`. A caption should be interpretable without reverse-engineering a methods paragraph, but should not duplicate every setup detail.

Use a descriptive title or take-home statement only if the plotted data support it. Preserve figure IDs when revising a manuscript unless renumbering is explicitly part of the task.

## Export and review

Inspect vector output and the raster preview at intended width. Check font embedding/rendering, equations, line/marker readability, legend overlap, whitespace, panel alignment and clipping. Test grayscale or redundant encodings where needed. Do not impose a universal journal DPI or exact column width without the current template.

Keep raw data, a plotting script, derived summary data and the final exports connected by reproducible parameters. A successful save is not a visual review.

## Bundled line-plot helper

Input schema:

```csv
x,method,seed,value
0,method-a,run-1,0.20
1,method-a,run-1,0.35
0,method-a,run-2,0.22
1,method-a,run-2,0.33
```

The values above are synthetic format examples, not paper evidence. Numeric x is required. Each `(method,seed,x)` must be unique. The helper rejects non-finite values and mixed run coverage, so every method has the same seed set at each of its x values; align incomplete trajectories explicitly before using it. Methods may have different x grids. Compare metrics/budgets yourself before plotting.

Example: `python scripts/plot_results.py actual_results.csv --outdir figures --xlabel "Elapsed time (s)" --ylabel "Test accuracy" --uncertainty std`. Labels are supplied by the user/data context, not inferred from the column name. Without `--uncertainty std`, no uncertainty shading is added.
