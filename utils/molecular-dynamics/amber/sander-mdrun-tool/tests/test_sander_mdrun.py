"""Tests for sander_mdrun."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_sander_mdrun() -> None:
    """Test sander_mdrun CWL."""
    cwl_file_str = "sander_mdrun.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    input_top_path = Path(__file__).resolve().parent / Path("cln025.prmtop")
    input_crd_path = Path(__file__).resolve().parent / Path("cln025.inpcrd")
    input_mdin_path = Path(__file__).resolve().parent / Path("npt.mdin")

    sander_mdrun = Step(clt_path=cwl_file)
    sander_mdrun.input_top_path = input_top_path
    sander_mdrun.input_crd_path = input_crd_path
    sander_mdrun.input_mdin_path = input_mdin_path
    sander_mdrun.output_log_path = "system.log"
    sander_mdrun.output_traj_path = "system.trj"
    sander_mdrun.output_rst_path = "system.rst"
    sander_mdrun.output_cpout_path = "system.cpout"
    sander_mdrun.output_cprst_path = "system.cprst"
    sander_mdrun.output_mdinfo_path = "system.mdinfo"

    steps = [sander_mdrun]
    filename = "sander_mdrun"
    viz = Workflow(steps, filename)

    viz.run()

    outdir = Path("outdir")
    files = list(outdir.rglob("system.rst"))

    assert (
        files
    ), f"The file 'system.rst' does not exist in any subdirectory of '{outdir}'."
