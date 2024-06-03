"""Test the sanitize_ligand plugin."""
import sys
from pathlib import Path

import pytest
from polus.mm.utils.sanitize_ligand import attempt_fix_ligand
from rdkit import Chem

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent.parent.parent / "cwl_utils"
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


def test_sanitize_ligand_cwl() -> None:
    """Test the pose_cluster_filter CWL."""
    cwl_file = Path("sanitize_ligand_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["input_small_mol_ligand"]["path"] = str(
        Path(__file__).resolve().parent / Path("4xk9_ligand.sdf"),
    )

    input_yaml_path = Path("sanitize_ligand_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert "success" in stderr
