"""Tests for sander_mdrun."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_sander_mdrun() -> None:
    """Test sander_mdrun."""
    cwl_file_str = "sander_mdrun.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "cln025.prmtop"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_top_path"]["path"] = file_path
    file_path_str = "cln025.inpcrd"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_crd_path"]["path"] = file_path
    file_path_str = "npt.mdin"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_mdin_path"]["path"] = file_path
    input_to_props["input_mdin_path"]["class"] = "File"
    del input_to_props["input_cpin_path"]
    del input_to_props["input_ref_path"]

    input_yaml_path = Path("sander_mdrun.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    print("stdout:", stdout)  # noqa: T201
    print("stderr:", stderr)  # noqa: T201

    assert Path("system.rst").exists()
