"""Tests for acpype."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_acpype() -> None:
    """Test acpype CWL."""
    # Define paths and input properties
    input_path = Path(__file__).resolve().parent / Path("5umx_ligand.sdf")
    cwl_file_str = "acpype.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    # Create the CWL step
    acpype_step = Step(clt_path=cwl_file)
    acpype_step.input_path = str(input_path)
    acpype_step.output_gro_path = "system.gro"
    acpype_step.output_itp_path = "system.itp"
    acpype_step.output_top_path = "system.top"
    acpype_step.base_name = "ligand"
    acpype_step.charge_method = "bcc"
    acpype_step.output_pdb_path = "system.pdb"

    # Create the workflow and run it
    steps = [acpype_step]
    filename = "acpype_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # Define the output directory and pattern
    outdir = Path("outdir")  # Output directory
    output_files = list(outdir.rglob("ligand_GMX.gro"))

    # Check if the expected output file exists
    assert (
        output_files
    ), f"No file matching pattern 'ligand_GMX.gro' found in '{outdir}'."
