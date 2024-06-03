"""Test the sanitize_ligand plugin."""
from pathlib import Path

import pytest
from polus.mm.utils.sanitize_ligand import attempt_fix_ligand
from rdkit import Chem
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


@pytest.mark.catch_error()
def test_kekulization_error_catch() -> None:
    """Test catching Kekulization error.

    Can't kekulize mol.  Unkekulized atoms: 6 7 8 9 10.
    """
    mol = Chem.MolFromSmiles("c1ccc(cc1)-c1nnc(n1)-c1ccccc1")
    valid_ligand, rdkit_mol = attempt_fix_ligand(mol)
    assert not valid_ligand


@pytest.mark.fix_ligand()
def test_fix_explicit_valence_error() -> None:
    """Test fixing explicit valence error.

    Explicit valence for atom # 1 C, 5, is greater than permitted
    """
    mol = Chem.MolFromSmiles("c1c(ccc2NC(CN=c(c21)(C)C)=O)O", sanitize=False)
    valid_ligand, rdkit_mol = attempt_fix_ligand(mol)
    assert valid_ligand


def test_sanitize_ligand_cwl() -> None:
    """Test the sanitize_ligand CWL."""
    cwl_file_str = "sanitize_ligand_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    input_ligand_path = Path(__file__).resolve().parent / Path("4xk9_ligand.sdf")

    sanitize_ligand = Step(clt_path=cwl_file)
    sanitize_ligand.input_small_mol_ligand = input_ligand_path

    steps = [sanitize_ligand]
    filename = "sanitize_ligand"
    viz = Workflow(steps, filename)

    viz.run()

    outdir = Path("outdir")
    output_files = list(outdir.rglob("*.sdf"))

    assert output_files, "No output SDF files were generated."

    # Check if the input SDF filename is part of the output
    input_filename = input_ligand_path.name
    output_filenames = [f.name for f in output_files]
    assert any(
        input_filename in of for of in output_filenames
    ), f"The input SDF file '{input_filename}' was not found in the output."
