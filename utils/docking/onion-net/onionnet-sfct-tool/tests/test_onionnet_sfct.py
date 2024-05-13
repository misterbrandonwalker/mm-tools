"""Tests for onionnet-sfct."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_onionnet_sfct() -> None:
    """Test onionnet-sfct."""
    # Define the CWL file path
    cwl_file = Path(__file__).resolve().parent / "onionnet_sfct_0@1@0.cwl"

    # Create a Step instance for onionnet-sfct
    onionnet_sfct_step = Step(clt_path=cwl_file)

    # Define input file paths
    receptor_path = str(Path(__file__).resolve().parent / "5uv2_protein.pdb")
    ligand_path = str(Path(__file__).resolve().parent / "5uv2_ligand.pdb")

    # Assign input paths to the step
    onionnet_sfct_step.receptor_path = receptor_path
    onionnet_sfct_step.ligand_path = ligand_path
    onionnet_sfct_step.output_path = "output"

    # Create a Workflow instance with the step
    steps = [onionnet_sfct_step]
    viz = Workflow(steps, "onionnet_sfct")

    # Run the workflow
    viz.run()

    # Check if the expected output file exists
    outdir = Path("outdir")
    files = list(outdir.rglob("system.mol2"))

    assert (
        files
    ), f"The file 'system.mol2' does not exist in any subdirectory of '{outdir}'."
