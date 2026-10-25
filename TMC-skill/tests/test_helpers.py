"""Observable input-integrity and serialization checks; all records/data are synthetic."""
import copy
import importlib.util
import math
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


citations = load("citation_export", "skills/tmc-citation/scripts/export_references.py")
figures = load("figure_plot", "skills/tmc-figure/scripts/plot_results.py")
corpus = load("corpus_inventory", "scripts/analyze_tmc_corpus.py")


def test_temp_dir():
    return tempfile.TemporaryDirectory(dir=os.environ.get("TMC_SKILL_TEST_TMP"))


class CitationTests(unittest.TestCase):
    def setUp(self):
        self.row = {"key": "Synthetic2026", "title": "Synthetic FL & PEFT_Study {Example}",
                    "authors": ["Example, Alice", "Sample, Bo"], "year": 2026,
                    "venue": "Synthetic Venue", "pages": "10-19", "type": "article",
                    "metadata_status": "verified", "checked_at": "2026-10-25",
                    "source_url": "https://example.org/synthetic-not-a-real-reference",
                    "doi": "https://doi.org/10.1234/SYNTHETIC_not-real"}

    def test_unchecked_metadata_is_rejected(self):
        self.row["metadata_status"] = "candidate"
        with self.assertRaises(ValueError):
            citations.validate([self.row])

    def test_missing_provenance_is_rejected(self):
        self.row.pop("source_url")
        with self.assertRaises(ValueError):
            citations.validate([self.row])

    def test_duplicate_doi_different_case_and_prefix_is_rejected(self):
        other = copy.deepcopy(self.row)
        other.update(key="Other", title="A different synthetic title", doi="doi:10.1234/synthetic_not-real")
        with self.assertRaises(ValueError):
            citations.validate([self.row, other])

    def test_export_preserves_names_and_identifier_but_escapes_prose(self):
        rows = citations.validate([self.row])
        bib = citations.export(rows, "bib")
        self.assertIn("Example, Alice and Sample, Bo", bib)
        self.assertIn(r"FL \& PEFT\_Study \{Example\}", bib)
        self.assertIn("10.1234/synthetic_not-real", bib)
        self.assertNotIn(r"synthetic\_not-real", bib)
        ris = citations.export(rows, "ris")
        self.assertIn("SP  - 10\nEP  - 19\nER  -", ris)
        enw = citations.export(rows, "enw")
        self.assertIn("%A Example, Alice\n%A Sample, Bo", enw)
        self.assertIn("%P 10-19", enw)
        self.assertEqual(rows[0]["support_status"], "metadata-only")


class FigureTests(unittest.TestCase):
    def read(self, text):
        with test_temp_dir() as folder:
            path = Path(folder) / "synthetic.csv"
            path.write_text(text, encoding="utf-8")
            return figures.read_results(path)

    def test_mean_sample_variation_and_single_run(self):
        result = self.read("x,method,seed,value\n0,A,1,1\n0,A,2,3\n1,A,1,3\n1,A,2,5\n0,B,1,2\n")
        self.assertEqual(result["A"][0]["mean"], 2)
        self.assertAlmostEqual(result["A"][0]["std"], math.sqrt(2))
        self.assertEqual(result["A"][0]["n"], 2)
        self.assertIsNone(result["B"][0]["std"])

    def test_duplicate_and_nonfinite_results_are_rejected(self):
        for rows in ["0,A,1,1\n0,A,1,2\n", "0,A,1,nan\n", "inf,A,1,2\n"]:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                self.read("x,method,seed,value\n" + rows)

    def test_missing_runs_are_not_silently_averaged(self):
        with self.assertRaises(ValueError):
            self.read("x,method,seed,value\n0,A,1,1\n0,A,2,3\n1,A,1,4\n")

    def test_empty_and_bad_headers_are_rejected(self):
        for text in ["x,method,seed,value\n", "x,value\n0,2\n"]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.read(text)

    def test_vector_and_raster_exports_and_summary(self):
        result = self.read("x,method,seed,value\n0,A,1,1\n0,A,2,3\n1,A,1,2\n1,A,2,4\n")
        with test_temp_dir() as folder:
            paths = figures.plot(result, folder, "Synthetic x", "Synthetic value", "std")
            self.assertTrue(all(p.is_file() and p.stat().st_size > 0 for p in paths))
            self.assertTrue(paths[0].read_bytes().startswith(b"%PDF"))
            self.assertIn("sample_std,n", paths[3].read_text(encoding="utf-8"))
            with self.assertRaises(ValueError):
                figures.plot(result, folder, "x", "y")

    def test_invalid_log_axes_are_rejected(self):
        result = self.read("x,method,seed,value\n0,A,1,1\n")
        with self.assertRaises(ValueError):
            figures.plot(result, "unused", "x", "y", xscale="log")


class CorpusTests(unittest.TestCase):
    def test_corrupt_pdf_is_recorded_as_error(self):
        with test_temp_dir() as folder:
            path = Path(folder) / "corrupt.pdf"
            path.write_bytes(b"not a PDF")
            result = corpus.analyze(path, Path(folder))
            self.assertEqual(result["status"], "error")
            self.assertIn("error", result)
            self.assertEqual(len(result["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
