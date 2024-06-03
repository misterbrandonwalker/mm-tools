"""Tests for random_subset_rows."""
from pathlib import Path

from polus.mm.utils.random_subset_rows.random_subset_rows import random_subset_rows
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_random_subset_rows() -> None:
    """Test random_subset_rows."""
    input_file = "rows.txt"
    num_of_samples = 2
    random_seed = 0
    output_file = "output.txt"
    path = Path(__file__).resolve().parent / Path(input_file)
    random_subset_rows(path, num_of_samples, random_seed, output_file)
    assert Path(output_file).exists()


def test_random_subset_rows_cwl() -> None:
    """Test random_subset_rows CWL."""
    cwl_file_str = "random_subset_rows_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    input_file_path = Path(__file__).resolve().parent / Path("rows.txt")

    random_subset_rows = Step(clt_path=cwl_file)
    random_subset_rows.input_file = input_file_path
    random_subset_rows.num_of_samples = 2
    random_subset_rows.random_seed = 0
    random_subset_rows.output_file = "cwl_output.txt"

    steps = [random_subset_rows]
    filename = "random_subset_rows"
    viz = Workflow(steps, filename)

    viz.run()

    outdir = Path("outdir")
    output_files = list(outdir.rglob("cwl_output.txt"))

    assert (
        output_files
    ), f"The file 'cwl_output.txt' does not exist in any subdirectory of '{outdir}'."
