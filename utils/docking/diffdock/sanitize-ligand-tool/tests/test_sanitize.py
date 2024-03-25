"""Test the sanitize_ligand plugin."""
import sys

sys.path.append("src")
from pathlib import Path  # noqa: E402

import pytest  # noqa: E402
from polus.mm.utils.sanitize_ligand import attempt_fix_ligand  # noqa: E402
from rdkit import Chem  # noqa: E402

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


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
    cwl_file = Path("sanitize_ligand.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    ligand_path = "ligand.sdf"
    ligand_path = str(Path(__file__).resolve().parent / Path(ligand_path))
    input_to_props["input_small_mol_ligand"]["path"] = ligand_path
    input_yaml_path = Path("sanitize_ligand.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    # TODO: cwltool cannot seem to overwrite the same filename?
    call_cwltool(cwl_file, input_yaml_path)

    assert Path("valid.txt").exists()
