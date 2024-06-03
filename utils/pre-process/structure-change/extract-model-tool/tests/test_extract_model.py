"""Tests for extract_model."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_extract_model() -> None:
    """Test extract_model."""
    # Define paths and input properties
    cwl_file_str = "extract_model_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_structure_path = Path(__file__).resolve().parent / Path("extract_model.pdb")
    config = '{"models": [1, 2, 3]}'

    # Create the CWL step
    extract_model_step = Step(clt_path=cwl_file)
    extract_model_step.input_structure_path = input_structure_path
    extract_model_step.output_structure_path = "system.pdb"
    extract_model_step.config = config

    # Create the workflow and run it
    steps = [extract_model_step]
    filename = "extract_model_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # Check for the expected output file
    outdir = Path("outdir")
    files = list(outdir.rglob("system.pdb"))

    assert (
        files
    ), f"The file 'system.pdb' does not exist in any subdirectory of '{outdir}'."
