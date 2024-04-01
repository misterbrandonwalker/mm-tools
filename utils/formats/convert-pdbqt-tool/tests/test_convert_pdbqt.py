"""Test the convert_pdbqt function."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import modify_cwl_file  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_convert_pdbqt() -> None:
    """Test the convert_pdbqt function."""
    format_dict = {"input_path": {"format": "edam:format_1476"}}
    modified_cwl_file = modify_cwl_file(Path("convert_pdbqt.cwl"), format_dict)
    input_to_props = parse_cwl_arguments(Path(modified_cwl_file))
    ligand_path = "ligand.sdf"
    ligand_path = str(Path(__file__).resolve().parent / Path(ligand_path))
    input_to_props["input_path"]["path"] = ligand_path
    input_yaml_path = Path("convert_pdbqt.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    call_cwltool(Path(modified_cwl_file), input_yaml_path)

    assert Path("system.pdbqt").exists()
