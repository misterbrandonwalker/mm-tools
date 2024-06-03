"""Tests for generate_conformers_sdf."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_generate_conformers_sdf() -> None:
    """Test generate_conformers_sdf."""
    cwl_file = Path("generate_conformers_sdf.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "5umx_ligand.sdf"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_path"]["path"] = file_path
    input_yaml_path = Path("generate_conformers_sdf.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path("system.sdf").exists()
