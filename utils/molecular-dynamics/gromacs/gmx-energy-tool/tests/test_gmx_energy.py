"""Tests for gmx_energy."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_gmx_energy() -> None:
    """Test gmx_energy."""
    # Define paths
    cwl_file_str = "gmx_energy_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_energy_path = Path(__file__).resolve().parent / Path("energy.edr")

    # Create the CWL step
    gmx_energy_step = Step(clt_path=cwl_file)
    gmx_energy_step.config = '{"terms": ["Potential"]}'
    gmx_energy_step.input_energy_path = input_energy_path
    gmx_energy_step.output_xvg_path = "system.xvg"

    # Create the workflow and run it
    steps = [gmx_energy_step]
    filename = "gmx_energy_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # Define output directory and check for expected output
    outdir = Path("outdir")
    files = list(outdir.rglob("system.xvg"))

    assert (
        files
    ), f"The file 'system.xvg' does not exist in any subdirectory of '{outdir}'."
