"""Tests for rename_residues_mol."""
import sys
from pathlib import Path

from polus.mm.utils.rename_residues_mol.rename_residues_mol import rename_residues_mol

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_rename_residues_mol() -> None:
    """Test rename_residues_mol."""
    input_mol2_path = "5umx_ligand.mol2"
    input_mol2_path_path = Path(__file__).resolve().parent / Path(input_mol2_path)
    output_mol2_path = "output.mol2"
    rename_residues_mol(input_mol2_path_path, output_mol2_path)
    assert Path(output_mol2_path).exists()


def test_rename_residues_mol_cwl() -> None:
    """Test rename_residues_mol CWL."""
    cwl_file_str = "rename_residues_mol_0.1.0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "5umx_ligand.mol2"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_mol2_path"]["path"] = file_path

    input_yaml_path = Path("rename_residues_mol_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert Path("system.mol2").exists()
