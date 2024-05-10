"""Tests for smina_docking."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_smina_docking() -> None:
    """Test smina_docking."""
    cwl_file = Path("smina_docking_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "5umx_protein.pdb"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["receptor_file"]["path"] = file_path
    input_to_props["receptor_file"]["class"] = "File"
    file_path_str = "5umx_ligand.sdf"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["ligand_file"]["path"] = file_path
    input_to_props["ligand_file"]["class"] = "File"
    input_to_props["ligand_box"]["path"] = file_path
    input_to_props["ligand_box"]["class"] = "File"
    input_yaml_path = Path("smina_docking_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert Path("string").exists()
