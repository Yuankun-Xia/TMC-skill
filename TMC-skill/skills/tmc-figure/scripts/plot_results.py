#!/usr/bin/env python3
"""Plot actual numeric-x CSV results; requires matplotlib. Never generates data."""
import argparse
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path


def read_results(path):
    groups = defaultdict(lambda: defaultdict(dict))
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not {"x", "method", "seed", "value"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV needs x,method,seed,value columns")
        for line, row in enumerate(reader, 2):
            try:
                x, value = float(row["x"]), float(row["value"])
                method, seed = row["method"].strip(), row["seed"].strip()
            except (TypeError, ValueError, AttributeError) as error:
                raise ValueError(f"invalid row at line {line}") from error
            if not method or not seed or not math.isfinite(x) or not math.isfinite(value):
                raise ValueError(f"empty identity or non-finite value at line {line}")
            if seed in groups[method][x]:
                raise ValueError(f"duplicate method/seed/x at line {line}")
            groups[method][x][seed] = value
    if not groups:
        raise ValueError("CSV has no result rows")
    summary = {}
    for method, by_x in groups.items():
        seed_sets = [set(runs) for runs in by_x.values()]
        if any(seeds != seed_sets[0] for seeds in seed_sets):
            raise ValueError(f"unequal seed coverage across x for {method}; align runs explicitly")
        summary[method] = []
        for x, runs in sorted(by_x.items()):
            values = list(runs.values())
            summary[method].append({"x": x, "n": len(values),
                                    "mean": statistics.mean(values),
                                    "std": statistics.stdev(values) if len(values) > 1 else None})
    return summary


def plot(summary, outdir, xlabel, ylabel, uncertainty="none", xscale="linear",
         yscale="linear", stem="results", overwrite=False):
    if not stem or Path(stem).name != stem or stem in {".", ".."}:
        raise ValueError("stem must be a filename without directory components")
    if xscale == "log" and any(r["x"] <= 0 for rows in summary.values() for r in rows):
        raise ValueError("log x requires positive x")
    if yscale == "log":
        for rows in summary.values():
            for row in rows:
                lower = row["mean"] - (row["std"] or 0) if uncertainty == "std" else row["mean"]
                if lower <= 0:
                    raise ValueError("log y requires positive means and shaded bounds")
    outdir = Path(outdir)
    paths = [outdir / f"{stem}.{ext}" for ext in ("pdf", "svg", "png", "csv")]
    if not overwrite and any(path.exists() for path in paths):
        raise ValueError("an output exists; choose another stem/directory or --overwrite")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    palette = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9", "#333333"]
    markers = ["o", "s", "^", "D", "v", "P", "X"]
    with plt.rc_context({"font.size": 9, "pdf.fonttype": 42, "ps.fonttype": 42,
                         "svg.fonttype": "none", "axes.spines.top": False,
                         "axes.spines.right": False}):
        fig, ax = plt.subplots(figsize=(3.5, 2.6), layout="constrained")
        for index, (method, rows) in enumerate(summary.items()):
            xs, means = [r["x"] for r in rows], [r["mean"] for r in rows]
            color = palette[index % len(palette)]
            ax.plot(xs, means, label=method, color=color,
                    marker=markers[index % len(markers)], markersize=3, linewidth=1.3)
            if uncertainty == "std":
                lower = [r["mean"] - r["std"] if r["std"] is not None else float("nan") for r in rows]
                upper = [r["mean"] + r["std"] if r["std"] is not None else float("nan") for r in rows]
                ax.fill_between(xs, lower, upper, color=color, alpha=0.16, linewidth=0)
        ax.set(xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale)
        ax.grid(alpha=0.18)
        ax.legend(frameon=False, fontsize=8)
        outdir.mkdir(parents=True, exist_ok=True)
        for path in paths[:3]:
            fig.savefig(path, dpi=300)
        plt.close(fig)
    with paths[3].open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["method", "x", "mean", "sample_std", "n"])
        for method, rows in summary.items():
            for row in rows:
                writer.writerow([method, row["x"], row["mean"],
                                 row["std"] if row["std"] is not None else "", row["n"]])
    return paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--outdir", required=True, type=Path)
    parser.add_argument("--xlabel", required=True)
    parser.add_argument("--ylabel", required=True)
    parser.add_argument("--uncertainty", choices=["none", "std"], default="none")
    parser.add_argument("--xscale", choices=["linear", "log"], default="linear")
    parser.add_argument("--yscale", choices=["linear", "log"], default="linear")
    parser.add_argument("--stem", default="results")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        paths = plot(read_results(args.csv), args.outdir, args.xlabel, args.ylabel,
                     args.uncertainty, args.xscale, args.yscale, args.stem, args.overwrite)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    for path in paths:
        print(path.resolve())


if __name__ == "__main__":
    main()
