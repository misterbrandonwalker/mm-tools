"""Tests for extract_model_pdbqt."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_extract_model_pdbqt() -> None:
    """Test extract_model_pdbqt."""
    # Define paths and input properties
    cwl_file_str = "extract_model_pdbqt_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_pdbqt_path = Path(__file__).resolve().parent / Path("models.pdbqt")

    # Create the CWL step
    extract_model_pdbqt_step = Step(clt_path=cwl_file)
    extract_model_pdbqt_step.input_pdbqt_path = input_pdbqt_path
    extract_model_pdbqt_step.output_pdbqt_path = "system.pdbqt"

    # Create the workflow and run it
    steps = [extract_model_pdbqt_step]
    filename = "extract_model_pdbqt_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # Check for the expected output file
    outdir = Path("outdir")
    files = list(outdir.rglob("system.pdbqt"))

    assert (
        files
    ), f"The file 'system.pdbqt' does not exist in any subdirectory of '{outdir}'."
