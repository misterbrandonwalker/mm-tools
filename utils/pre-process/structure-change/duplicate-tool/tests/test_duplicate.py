"""Tests for duplicate."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_duplicate() -> None:
    """Test pdb."""
    # Define paths and input properties
    cwl_file_str = "duplicate_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_pdbqt_singleton_path = Path(__file__).resolve().parent / Path(
        "1msn_protein.pdb",
    )
    repeats = 2

    # Create the CWL step
    duplicate_step = Step(clt_path=cwl_file)
    duplicate_step.input_pdbqt_singleton_path = input_pdbqt_singleton_path

    # Prepare the input_pdbqt_array_path with duplicates
    file_dict = {"path": str(input_pdbqt_singleton_path)}
    duplicate_step.input_pdbqt_array_path = [file_dict.copy() for _ in range(repeats)]

    # Create the workflow and run it
    steps = [duplicate_step]
    filename = "duplicate_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # cant capture stdout to check status
