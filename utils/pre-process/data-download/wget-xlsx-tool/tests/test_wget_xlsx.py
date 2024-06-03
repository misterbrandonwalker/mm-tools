"""Test the wget_xlsx tool."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_wget_xlsx() -> None:
    """Test wget_xlsx."""
    cwl_file_str = "wget_xlsx_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    wget_xlsx = Step(clt_path=cwl_file)
    wget_xlsx.url = "https://smacc.mml.unc.edu/ncats_target_based_curated.xlsx"
    wget_xlsx.output_xlsx_path = "system.xlsx"

    steps = [wget_xlsx]
    filename = "wget_xlsx"
    viz = Workflow(steps, filename)

    viz.run()

    outdir = Path("outdir")
    files = list(outdir.rglob("system.xlsx"))

    assert (
        files
    ), f"The file 'system.xlsx' does not exist in any subdirectory of '{outdir}'."
