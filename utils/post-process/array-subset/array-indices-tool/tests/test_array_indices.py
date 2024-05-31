"""Tests for array_indices."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_array_indices() -> None:
    """Test array_indices."""
    # Define paths and input properties
    cwl_file_str = "array_indices_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_props = {"input_indices": [1, 3], "input_array": [1, 2, 3, 4, 5]}

    # Create the CWL step
    array_indices_step = Step(clt_path=cwl_file)
    array_indices_step.input_indices = input_props["input_indices"]
    array_indices_step.input_array = input_props["input_array"]

    # Create the workflow and run it
    steps = [array_indices_step]
    filename = "array_indices_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # cant process the output since no way to grab stdout
