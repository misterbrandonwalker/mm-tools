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


def test_cwl_sanitize_ligand() -> None:
    """Test the convert_pdbqt function."""
    cwl_file = Path("sanitize_ligand_0@1@0.cwl")
    ligand_path = "ligand.sdf"
    ligand_path = str(Path(__file__).resolve().parent / Path(ligand_path))
    sanitize_ligand_step = Step(clt_path=cwl_file)
    sanitize_ligand_step.input_small_mol_ligand = ligand_path

    steps = [sanitize_ligand_step]
    filename = "sanitize_ligand"
    workflow = Workflow(steps, filename)

    workflow.run()

    outdir = Path("outdir")
    files = list(outdir.rglob("ligand.sdf"))

    assert (
        files
    ), f"The file ligand.sdf does not exist in any subdirectory of '{outdir}'."
