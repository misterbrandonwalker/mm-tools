"""Tests for combine_structure."""
import sys
from pathlib import Path

from polus.mm.utils.combine_structure.combine_structure import combine_structure

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_combine_structure() -> None:
    """Test combine_structure."""
    input_structure1 = Path(__file__).resolve().parent / Path("5umx_protein.xyz")
    input_structure2 = Path(__file__).resolve().parent / Path("5umx_ligand.xyz")
    output_structure_path = "combined_structure.xyz"
    combine_structure(input_structure1, input_structure2, output_structure_path)
    assert Path(output_structure_path).exists()


def test_combine_structure_cwl() -> None:
    """Test combine_structure CWL."""
    input_structure1 = Path(__file__).resolve().parent / Path("5umx_protein.xyz")
    input_structure2 = Path(__file__).resolve().parent / Path("5umx_ligand.xyz")
    output_structure_path = "combined_structure.xyz"
    cwl_file_str = "combine_structure_0.1.0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["input_structure1"]["path"] = str(input_structure1)
    input_to_props["input_structure2"]["path"] = str(input_structure2)
    input_yaml_path = Path("combine_structure_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path(output_structure_path).exists()
    Path(output_structure_path).unlink()
