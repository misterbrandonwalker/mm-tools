"""Tests for filter_array."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_filter_array() -> None:
    """Test filter_array."""
    # Define paths and input properties
    cwl_file_str = "filter_array_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_array = [1, 2, 3]
    input_bool_array = [False, True, False]

    # Create the CWL step
    filter_array_step = Step(clt_path=cwl_file)
    filter_array_step.input_array = input_array
    filter_array_step.input_bool_array = input_bool_array

    # Create the workflow and run it
    steps = [filter_array_step]
    filename = "filter_array_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # cant parse stdout
