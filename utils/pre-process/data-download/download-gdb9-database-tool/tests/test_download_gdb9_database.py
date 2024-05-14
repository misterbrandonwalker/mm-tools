"""Tests for download_gdb9_database."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_download_gdb9_database() -> None:
    """Test download_gdb9_database."""
    cwl_file = Path("download_gdb9_database_0@1@0.cwl")

    # Create the step for the CWL file
    download_gdb9_step = Step(clt_path=cwl_file)
    download_gdb9_step.output_sdf_path = "system.sdf"
    download_gdb9_step.output_NP_Score_path = "NP.gz"
    download_gdb9_step.output_SA_Score_path = "SA.gz"

    # Define the workflow with the step
    steps = [download_gdb9_step]
    filename = "download_gdb9_database_workflow"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "SA.gz" for file in outdir.rglob("*")
    ), "The file SA.gz was not found."
