"""Tests for pdbbind_refined_v2020_download."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_extract_pdbbind_refined() -> None:
    """Test extract_pdbbind_refined CWL."""
    cwl_file = Path("extract_pdbbind_refined_0@1@0.cwl")

    extract_pdbbind_refined_step = Step(clt_path=cwl_file)

    extract_pdbbind_refined_step.query = '(Kd_Ki == "Kd") and (value < 0.001)'
    extract_pdbbind_refined_step.convert_Kd_dG = True
    extract_pdbbind_refined_step.max_row = 1
    extract_pdbbind_refined_step.script = "/generate_pdbbind_complex.py"
    extract_pdbbind_refined_step.index_file_name = "INDEX_refined_data.2020"
    extract_pdbbind_refined_step.base_dir = "/refined-set"
    extract_pdbbind_refined_step.output_txt_path = "system.log"
    extract_pdbbind_refined_step.convert_Kd_dG = True

    steps = [extract_pdbbind_refined_step]
    filename = "extract_pdbbind_refined_workflow"
    workflow = Workflow(steps, filename)

    workflow.run()

    outdir = Path("outdir")
    assert any(
        file.name == "1e3g_protein.pdb" for file in outdir.rglob("*")
    ), "The file 1e3g_protein.pdb was not found."
