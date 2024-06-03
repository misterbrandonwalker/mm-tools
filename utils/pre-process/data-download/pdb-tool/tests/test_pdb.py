"""Tests for pdb."""
import json
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_pdb() -> None:
    """Test pdb CWL."""
    # Define file paths
    cwl_file_str = "pdb_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent / Path(cwl_file_str)
    input_yaml_path = Path("pdb.yml")

    # Define configuration
    config = {"pdb_code": "1e3g", "filter": False}
    config_json = json.dumps(config)

    # Create CWLWorkflow and configure it
    pdb_step = Step(clt_path=cwl_file)
    pdb_step.config = config_json
    pdb_step.input_yaml_path = input_yaml_path

    # Create Workflow
    steps = [pdb_step]
    workflow_name = "pdb_workflow"
    workflow = Workflow(steps, workflow_name)

    # Run Workflow
    workflow.run()

    # Check if output file exists
    outdir = Path(".")
    files = list(outdir.rglob("system.pdb"))

    assert (
        files
    ), f"The file 'system.pdb' does not exist in any subdirectory of '{outdir}'."
