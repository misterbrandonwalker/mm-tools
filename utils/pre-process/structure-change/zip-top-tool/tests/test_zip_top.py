"""Tests for zip_top."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_zip_top() -> None:
    """Test zip topology CWL."""
    input_top_path = Path(__file__).resolve().parent / Path(
        "ALL.Ala115Pro_step8_gio_gio.top",
    )
    input_itp_path = Path(__file__).resolve().parent / Path(
        "ALL.Ala115Pro_step4_p2g_p2g_Protein_chain_A.itp",
    )
    cwl_file_str = "zip_top_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    zip_top = Step(clt_path=cwl_file)
    zip_top.input_top_path = input_top_path
    zip_top.input_itp_path = input_itp_path
    zip_top.output_top_zip_path = "system.zip"

    steps = [zip_top]
    filename = "zip_top"
    viz = Workflow(steps, filename)

    viz.run()

    outdir = Path("outdir")
    files = list(outdir.rglob("system.zip"))

    assert (
        files
    ), f"The file 'system.zip' does not exist in any subdirectory of '{outdir}'."
