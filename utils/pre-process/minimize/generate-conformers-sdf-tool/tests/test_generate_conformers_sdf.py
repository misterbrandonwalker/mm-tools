"""Tests for generate_conformers_sdf."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_generate_conformers_sdf() -> None:
    """Test generate_conformers_sdf."""
    # Define paths
    cwl_file_str = "generate_conformers_sdf_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_path = Path(__file__).resolve().parent / Path("5umx_ligand.sdf")

    # Create the CWL step
    generate_conformers_step = Step(clt_path=cwl_file)
    generate_conformers_step.input_path = input_path
    generate_conformers_step.output_sdf_path = "system.sdf"

    # Create the workflow and run it
    steps = [generate_conformers_step]
    filename = "generate_conformers_sdf_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # Define output directory and check for expected output
    outdir = Path("outdir")
    files = list(outdir.rglob("system.sdf"))

    assert (
        files
    ), f"The file 'system.sdf' does not exist in any subdirectory of '{outdir}'."
