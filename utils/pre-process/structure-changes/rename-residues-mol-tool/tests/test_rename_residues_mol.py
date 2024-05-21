"""Tests for rename_residues_mol."""
from pathlib import Path

from polus.mm.utils.rename_residues_mol.rename_residues_mol import rename_residues_mol
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_rename_residues_mol() -> None:
    """Test rename_residues_mol."""
    input_mol2_path = "5umx_ligand.mol2"
    input_mol2_path_path = Path(__file__).resolve().parent / Path(input_mol2_path)
    output_mol2_path = "output.mol2"
    rename_residues_mol(input_mol2_path_path, output_mol2_path)
    assert Path(output_mol2_path).exists()


def test_rename_residues_mol_cwl() -> None:
    """Test rename_residues_mol CWL."""
    cwl_file_str = "rename_residues_mol_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    # Create a Step instance
    rename_residues_step = Step(clt_path=cwl_file)

    # Define input paths
    input_mol2_path = Path(__file__).resolve().parent / "5umx_ligand.mol2"
    rename_residues_step.input_mol2_path = input_mol2_path
    rename_residues_step.output_mol2_path = "system.mol2"

    # Create a Workflow instance
    steps = [rename_residues_step]
    viz = Workflow(steps, "rename_residues_mol")

    # Run the workflow
    viz.run()

    # Check if the expected output file exists
    outdir = Path("outdir")
    files = list(outdir.rglob("system.mol2"))

    assert (
        files
    ), f"The file 'system.mol2' does not exist in any subdirectory of '{outdir}'."
