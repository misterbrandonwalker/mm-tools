"""Tests for append_ligand."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_append_ligand_cwl() -> None:
    """Test append_ligand CWL."""
    # Define paths and input properties
    input_top_zip_path = Path(__file__).resolve().parent / Path("ndx2resttop.zip")
    input_itp_path = Path(__file__).resolve().parent / Path("pep_ligand.itp")
    cwl_file_str = "append_ligand_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    # Create the CWL step
    append_ligand_step = Step(clt_path=cwl_file)
    append_ligand_step.input_top_zip_path = str(input_top_zip_path)
    append_ligand_step.input_itp_path = str(input_itp_path)
    append_ligand_step.output_top_zip_path = "system.zip"

    # Create the workflow and run it
    steps = [append_ligand_step]
    filename = "append_ligand_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    outdir = Path("outdir")
    files = list(outdir.rglob("system.zip"))
    assert files, f"No file matching pattern 'system.zip' found in '{outdir}'."
