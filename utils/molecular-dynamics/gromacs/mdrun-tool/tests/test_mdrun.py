"""Tests for mdrun."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_mdrun() -> None:
    """Test mdrun."""
    # Define paths and setup input properties
    cwl_file_str = "mdrun_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    file_path_str = "mdrun.tpr"
    file_path = Path(__file__).resolve().parent / Path(file_path_str)

    # Create the CWL step
    mdrun_step = Step(clt_path=cwl_file)
    mdrun_step.input_tpr_path = file_path
    mdrun_step.output_crd_path = "system.gro"
    mdrun_step.output_edr_path = "system.edr"
    mdrun_step.output_log_path = "system.log"
    mdrun_step.output_trr_path = "system.trr"
    mdrun_step.output_xtc_path = "system.xtc"
    mdrun_step.output_cpt_path = "system.cpt"
    mdrun_step.output_dhdl_path = "system.xvg"

    # Create the workflow and run it
    steps = [mdrun_step]
    filename = "mdrun_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # Define output directory and check for expected output
    outdir = Path("outdir")
    files = list(outdir.rglob("system.trr"))

    assert (
        files
    ), f"The file 'system.trr' does not exist in any subdirectory of '{outdir}'."
