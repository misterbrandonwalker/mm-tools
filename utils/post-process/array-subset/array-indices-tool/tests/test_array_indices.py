"""Tests for array_indices."""
import json
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_array_indices() -> None:
    """Test array_indices."""
    cwl_file = Path("array_indices.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["input_indices"] = [1, 3]
    input_to_props["input_array"] = [1, 2, 3, 4, 5]
    input_yaml_path = Path("array_indices.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    output_data = json.loads(stdout)
    output_array = output_data["output_array"]
    assert output_array == [2, 4]
