"""Tests for smina_docking."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_smina_docking() -> None:
    """Test smina_docking."""
    cwl_file = Path("smina_docking_0@1@0.cwl")

    # Create the step for the CWL file
    smina_docking_step = Step(clt_path=cwl_file)

    # Set up the inputs for the step
    receptor_file_path = str(Path(__file__).resolve().parent / "5umx_protein.pdb")
    ligand_file_path = str(Path(__file__).resolve().parent / "5umx_ligand.sdf")

    smina_docking_step.receptor_file = receptor_file_path
    smina_docking_step.ligand_file = ligand_file_path
    smina_docking_step.ligand_box = ligand_file_path
    smina_docking_step.output_path = "output"

    # Define the workflow with the step
    steps = [smina_docking_step]
    filename = "smina_docking_workflow"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "output" for file in outdir.rglob("*")
    ), "The file string was not found."
