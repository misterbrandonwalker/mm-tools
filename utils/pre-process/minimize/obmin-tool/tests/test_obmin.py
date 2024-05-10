"""Tests for obmin."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_obmin() -> None:
    """Test obmin."""
    cwl_file = Path("obmin_0@1@0.cwl")

    # Create the step for the CWL file
    obmin_step = Step(clt_path=cwl_file)

    # Set up the inputs for the step
    obmin_step.script = "/obminimize.sh"
    obmin_step.input_mol2_path = str(Path(__file__).resolve().parent / "benzene.mol2")
    obmin_step.output_mol2_path = "system.mol2"

    # Define the workflow with the step
    steps = [obmin_step]
    filename = "obmin_workflow"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "system.mol2" for file in outdir.rglob("*")
    ), "The file system.mol2 was not found."
