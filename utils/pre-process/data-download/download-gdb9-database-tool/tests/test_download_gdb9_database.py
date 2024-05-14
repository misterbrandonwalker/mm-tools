"""Tests for download_gdb9_database."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_download_gdb9_database() -> None:
    """Test download_gdb9_database."""
    cwl_file = Path("download_gdb9_database_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    input_yaml_path = Path("download_gdb9_database_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path("SA.gz").exists()
