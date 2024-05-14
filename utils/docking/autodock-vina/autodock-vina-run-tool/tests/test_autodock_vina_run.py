"""Tests for autodock_vina_run."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_autodock_vina_run() -> None:
    """Test autodock_vina_run."""
    cwl_file = Path("autodock_vina_run_0@1@0.cwl")

    # Create the step for the CWL file
    autodock_vina_step = Step(clt_path=cwl_file)

    # Set up the inputs for the step
    ligand_file_path = str(Path(__file__).resolve().parent / "vina_ligand.pdbqt")
    receptor_file_path = str(Path(__file__).resolve().parent / "vina_receptor.pdbqt")
    box_file_path = str(Path(__file__).resolve().parent / "vina_box.pdb")

    autodock_vina_step.input_ligand_pdbqt_path = ligand_file_path
    autodock_vina_step.input_receptor_pdbqt_path = receptor_file_path
    autodock_vina_step.input_box_path = box_file_path
    autodock_vina_step.output_log_path = "system.log"
    autodock_vina_step.output_pdbqt_path = "system.pdbqt"

    # Define the workflow with the step
    steps = [autodock_vina_step]
    filename = "autodock_vina_workflow"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "system.pdbqt" for file in outdir.rglob("*")
    ), "The file system.pdbqt was not found."
