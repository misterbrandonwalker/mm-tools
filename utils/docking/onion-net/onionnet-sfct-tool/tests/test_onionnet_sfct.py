"""Tests for onionnet-sfct."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_onionnet_sfct() -> None:
    """Test onionnet-sfct."""
    cwl_file = Path("onionnet-sfct_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "5uv2_protein.pdb"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["receptor_path"]["path"] = file_path
    input_to_props["receptor_path"]["class"] = "File"
    file_path_str = "5uv2_ligand.pdb"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["ligand_path"]["path"] = file_path
    input_to_props["ligand_path"]["class"] = "File"
    input_yaml_path = Path("onionnet-sfct_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert Path("system.mol2").exists()
