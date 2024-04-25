"""Tests for diffdock."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_diffdock() -> None:
    """Test diffdock."""
    cwl_file = Path(__file__).resolve().parent.parent / "diffdock_0@1@0.cwl"

    # Create a Step instance
    diffdock_step = Step(clt_path=cwl_file)

    # Define input paths
    protein_path = str(Path(__file__).resolve().parent / "5umx_protein.pdb")
    ligand_path = str(Path(__file__).resolve().parent / "5umx_ligand.sdf")

    # Assign inputs to the step
    diffdock_step.protein_path = protein_path
    diffdock_step.ligand_path = ligand_path

    # Create a Workflow instance
    steps = [diffdock_step]
    viz = Workflow(steps, "diffdock")

    # Run the workflow
    viz.run()

    # Check if the expected output file exists
    outdir = Path("outdir")
    files = list(outdir.rglob("rank1.sdf"))

    assert (
        files
    ), f"The file 'rank1.sdf' does not exist in any subdirectory of '{outdir}'."
