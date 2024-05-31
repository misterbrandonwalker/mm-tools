"""Tests for append_ligand."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_append_ligand_cwl() -> None:
    """Test combine_structure CWL."""
    input_top_zip_path = Path(__file__).resolve().parent / Path("ndx2resttop.zip")
    input_itp_path = Path(__file__).resolve().parent / Path("pep_ligand.itp")
    cwl_file_str = "append_ligand.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["input_top_zip_path"]["path"] = str(input_top_zip_path)
    input_to_props["input_itp_path"]["path"] = str(input_itp_path)
    del input_to_props["input_posres_itp_path"]  # optional file dont need to givel
    input_yaml_path = Path("append_ligand.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert Path("system.zip").exists()
