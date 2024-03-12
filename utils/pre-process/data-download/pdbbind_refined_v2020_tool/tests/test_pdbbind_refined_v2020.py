"""Tests for pdbbind_refined_v2020."""
import sys
from pathlib import Path

sys.path.append("src")
from polus.mm.utils.pdbbind_refined_v2020.pdbbind_refined_v2020 import (  # noqa: E402
    pdbbind_refined_v2020,
)

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_pdbbind_refined_v2020() -> None:
    """Test pdbbind_refined_v2020."""
    output_txt_path = "output.txt"
    index_file_name = "INDEX_refined_data.2020"
    base_dir = Path.cwd() / "refined-set"
    query = '(Kd_Ki == "Kd") and (value < 0.001)'
    min_row = 1
    max_row = 1
    convert_kd_dg = True
    pdbbind_refined_v2020(
        output_txt_path,
        index_file_name,
        base_dir,
        query,
        min_row,
        max_row,
        convert_kd_dg,
    )
    current_directory = Path.cwd()  # Get the current directory
    pdb_files = list(current_directory.glob("*.pdb"))  # List all *.pdb files
    sdf_files = list(current_directory.glob("*.sdf"))  # List all *.sdf files

    assert pdb_files, "No .pdb files found in the directory"
    assert sdf_files, "No .sdf files found in the directory"


def test_extract_pdbbind_refined() -> None:
    """Test pdb."""
    cwl_file = Path("extract_pdbbind_refined_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["query"] = '(Kd_Ki == "Kd") and (value < 0.001)'
    input_to_props["convert_Kd_dG"] = True
    input_to_props["max_row"] = 1
    input_yaml_path = Path("extract_pdbbind_refined_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)

    assert Path("1e3g_protein.pdb").is_file()
