"""Tests for the GROMACS grompp tool."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_grompp_cwl() -> None:
    """Tests grompp.cwl."""
    # Define paths and setup input properties
    cwl_file_str = "grompp_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    input_crd_path = Path(__file__).resolve().parent / Path("grompp.gro")
    input_top_zip_path = Path(__file__).resolve().parent / Path("grompp.zip")

    # Create the CWL step
    grompp_step = Step(clt_path=cwl_file)
    grompp_step.input_crd_path = input_crd_path
    grompp_step.input_top_zip_path = input_top_zip_path
    grompp_step.output_tpr_path = "system.tpr"

    # Create the workflow and run it
    steps = [grompp_step]
    filename = "grompp_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # Define output directory and check for expected output
    outdir = Path("outdir")
    files = list(outdir.rglob("system.tpr"))

    assert (
        files
    ), f"The file 'system.tpr' does not exist in any subdirectory of '{outdir}'."
