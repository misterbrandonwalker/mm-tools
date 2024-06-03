"""Tests for pdb."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_pdb() -> None:
    """Test pdb."""
    cwl_file = Path("pdb.cwl")
    config = '{"pdb_code":"1e3g","filter":false}'
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["config"] = config
    input_yaml_path = Path("pdb.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    call_cwltool(cwl_file, input_yaml_path)

    assert Path("system.pdb").is_file()
