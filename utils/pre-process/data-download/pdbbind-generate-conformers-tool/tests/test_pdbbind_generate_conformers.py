"""Tests for pdbbind_generate_conformers."""
from pathlib import Path

from polus.mm.utils.pdbbind_generate_conformers.pdbbind_generate_conformers import (
    pdbbind_generate_conformers,
)
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


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
    cwl_file = Path("pdbbind_generate_conformers_0@1@0.cwl")

    pdbbind_generate_conformers_step = Step(clt_path=cwl_file)
    pdbbind_generate_conformers_step.input_excel_path = str(
        Path(__file__).resolve().parent / Path("ncats_target_based_curated.xlsx"),
    )
    pdbbind_generate_conformers_step.query = (
        "`Standard Type` == 'Kd' and `duplicate-type-classifier` == 'unique'"
    )
    pdbbind_generate_conformers_step.smiles_column = "SMILES"
    pdbbind_generate_conformers_step.binding_data_column = "Standard Value"
    pdbbind_generate_conformers_step.convert_kd_dg = True
    pdbbind_generate_conformers_step.min_row = 1
    pdbbind_generate_conformers_step.max_row = 1
    pdbbind_generate_conformers_step.output_txt_path = "system.log"

    steps = [pdbbind_generate_conformers_step]
    filename = "pdbbind_generate_conformers"
    workflow = Workflow(steps, filename)

    workflow.run()

    outdir = Path("outdir")
    files = list(outdir.rglob("ligand_0.sdf"))

    assert (
        files
    ), f"The file 'ligand_0.sdf' does not exist in any subdirectory of '{outdir}'."
