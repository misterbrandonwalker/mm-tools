"""Tests for zip_top."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_zip_top() -> None:
    """Test zip topology CWL."""
    input_top_path = Path(__file__).resolve().parent / Path(
        "ALL.Ala115Pro_step8_gio_gio.top",
    )
    input_itp_path = Path(__file__).resolve().parent / Path(
        "ALL.Ala115Pro_step4_p2g_p2g_Protein_chain_A.itp",
    )
    cwl_file_str = "zip_top.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["input_top_path"]["path"] = str(input_top_path)
    input_to_props["input_itp_path"]["path"] = str(input_itp_path)
    input_to_props["input_itp_path"]["class"] = "File"
    input_yaml_path = Path("zip_top.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert Path("system.zip").exists()
