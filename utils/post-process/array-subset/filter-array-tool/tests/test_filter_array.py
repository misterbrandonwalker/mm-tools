"""Tests for filter_array."""
import json
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_filter_array() -> None:
    """Test filter_array."""
    cwl_file_str = "filter_array.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["input_array"] = [1, 2, 3]
    input_to_props["input_bool_array"] = [False, True, False]
    input_yaml_path = Path("filter_array.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    stdout_output, stderr = call_cwltool(cwl_file, input_yaml_path)
    output_dict = json.loads(stdout_output)
    output_array = output_dict.get("output_array", [])
    assert output_array == [2]
