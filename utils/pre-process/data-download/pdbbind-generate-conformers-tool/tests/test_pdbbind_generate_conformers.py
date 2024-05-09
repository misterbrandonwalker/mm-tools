"""Tests for pdbbind_generate_conformers."""
import sys
from pathlib import Path

from polus.mm.utils.pdbbind_generate_conformers.pdbbind_generate_conformers import (
    pdbbind_generate_conformers,
)

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_pdbbind_generate_conformers() -> None:
    """Test pdbbind_generate_conformers."""
    input_excel_path = "ncats_target_based_curated.xlsx"
    path = Path(__file__).resolve().parent / Path(input_excel_path)
    query = "`Standard Type` == 'Kd' and `duplicate-type-classifier` == 'unique'"
    output_txt_path = "binding_data.txt"
    min_row = 1
    max_row = 1
    smiles_column = "SMILES"
    binding_data_column = "Standard Value"
    convert_kd_dg = True

    pdbbind_generate_conformers(
        path,
        query,
        output_txt_path,
        min_row,
        max_row,
        smiles_column,
        binding_data_column,
        convert_kd_dg,
    )
    assert Path("binding_data.txt").exists()


def test_pdbbind_generate_conformers_cwl() -> None:
    """Test pdbbind_generate_conformers CWL."""
    cwl_file = Path("pdbbind_generate_conformers_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    input_excel_path = "ncats_target_based_curated.xlsx"
    input_to_props["input_excel_path"]["path"] = str(
        Path(__file__).resolve().parent / Path(input_excel_path),
    )
    input_to_props[
        "query"
    ] = "`Standard Type` == 'Kd' and `duplicate-type-classifier` == 'unique'"
    input_to_props["smiles_column"] = "SMILES"
    input_to_props["binding_data_column"] = "Standard Value"
    input_to_props["convert_kd_dg"] = True
    input_to_props["min_row"] = 1
    input_to_props["max_row"] = 1

    input_yaml_path = Path("pdbbind_generate_conformers_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path("ligand_0.sdf").exists()
