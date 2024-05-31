"""Tests for combine_structure."""
from pathlib import Path

from polus.mm.utils.combine_structure.combine_structure import combine_structure
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_combine_structure() -> None:
    """Test combine_structure."""
    input_structure1 = Path(__file__).resolve().parent / Path("5umx_protein.xyz")
    input_structure2 = Path(__file__).resolve().parent / Path("5umx_ligand.xyz")
    output_structure_path = "combined_structure.xyz"
    combine_structure(input_structure1, input_structure2, output_structure_path)
    assert Path(output_structure_path).exists()


def test_combine_structure_cwl() -> None:
    """Test combine_structure CWL."""
    # Define paths and input properties
    input_structure1 = Path(__file__).resolve().parent / Path("5umx_protein.xyz")
    input_structure2 = Path(__file__).resolve().parent / Path("5umx_ligand.xyz")
    output_structure_path = "combined_structure.xyz"
    cwl_file_str = "combine_structure_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    # Create the CWL step
    combine_structure_step = Step(clt_path=cwl_file)
    combine_structure_step.input_structure1 = str(input_structure1)
    combine_structure_step.input_structure2 = str(input_structure2)
    combine_structure_step.output_structure_path = "system.pdb"

    # Create the workflow and run it
    steps = [combine_structure_step]
    filename = "combine_structure_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # Check for the expected output
    assert Path(output_structure_path).exists()
    Path(output_structure_path).unlink()  # Clean up the output file
