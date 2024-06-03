"""Tests for wget_xlsx."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_wget_xlsx() -> None:
    """Test wget_xlsx."""
    cwl_file_str = "wget_xlsx.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["url"] = " https://smacc.mml.unc.edu/ncats_target_based_curated.xlsx"

    input_yaml_path = Path("wget_xlsx.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    call_cwltool(cwl_file, input_yaml_path)

    assert Path("system.xlsx").exists()
