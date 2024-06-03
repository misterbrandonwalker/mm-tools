"""Tests for grompp."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_grompp_cwl() -> None:
    """Tests grompp.cwl."""
    cwl_file_str = "grompp.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "grompp.gro"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_crd_path"]["path"] = file_path
    input_to_props["input_crd_path"]["class"] = "File"
    file_path_str = "grompp.zip"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_top_zip_path"]["path"] = file_path
    input_to_props["input_top_zip_path"]["class"] = "File"
    del input_to_props["input_cpt_path"]
    del input_to_props["input_ndx_path"]
    del input_to_props["input_mdp_path"]

    input_yaml_path = Path("grompp.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)

    assert Path("system.tpr").exists()
