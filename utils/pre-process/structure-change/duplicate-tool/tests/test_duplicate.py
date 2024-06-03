"""Tests for duplicate."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_duplicate() -> None:
    """Test pdb."""
    cwl_file_str = "duplicate.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "1msn_protein.pdb"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_pdbqt_singleton_path"]["path"] = file_path
    file_dict = input_to_props["input_pdbqt_array_path"][0]
    repeats = 2
    input_to_props["input_pdbqt_array_path"] = []
    for i in range(repeats):  # noqa: B007
        file_dict["path"] = file_path
        input_to_props["input_pdbqt_array_path"].append(file_dict)
    input_yaml_path = Path("pdb.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    # Just make sure calling cwltool doesnt crash since no outputs
    # This cwl file is just outputting duplicates in an array
    call_cwltool(cwl_file, input_yaml_path)
