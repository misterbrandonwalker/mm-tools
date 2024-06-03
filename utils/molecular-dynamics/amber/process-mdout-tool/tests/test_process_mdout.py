"""Tests for process_mdout."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_process_mdout() -> None:
    """Test process_mdout CWL."""
    cwl_file_str = "process_mdout_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    input_log_path = Path(__file__).resolve().parent / Path("sander.heat.log")

    process_mdout = Step(clt_path=cwl_file)
    process_mdout.input_log_path = input_log_path
    process_mdout.output_dat_path = "system.dat"

    steps = [process_mdout]
    filename = "process_mdout"
    viz = Workflow(steps, filename)

    viz.run()

    outdir = Path("outdir")
    output_files = list(outdir.rglob("system.dat"))

    assert (
        output_files
    ), f"The file 'system.dat' does not exist in any subdirectory of '{outdir}'."
