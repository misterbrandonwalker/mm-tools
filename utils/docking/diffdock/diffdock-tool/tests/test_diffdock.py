"""Tests for diffdock."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_diffdock() -> None:
    """Test diffdock."""
    cwl_file_str = "diffdock.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "5umx_protein.pdb"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["protein_path"]["path"] = file_path
    file_path_str = "5umx_ligand.sdf"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["ligand_path"]["path"] = file_path

    input_yaml_path = Path("diffdock.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert Path("rank1.sdf").exists()
