"""Tests for bash_top."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_bash_top() -> None:
    """Test bash topology CWL."""
    input_top_path = Path(__file__).resolve().parent / Path(
        "ALL.Ala115Pro_step8_gio_gio.top",
    )
    cwl_file_str = "bash_top.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    bash_top = Step(clt_path=cwl_file)
    bash_top.script = "/gmx_add_topology_includes.sh"
    bash_top.input_top_path = input_top_path

    steps = [bash_top]
    filename = "bash_top"
    viz = Workflow(steps, filename)
    # need a way to call cwl-docker-extract via run_local
    # Get the following error
    # TypeError: run() got an unexpected keyword argument 'run_local'
    viz.run(run_local=True)

    outdir = Path("outdir")
    files = list(outdir.rglob("system.top"))

    assert (
        files
    ), f"The file 'system.top' does not exist in any subdirectory of '{outdir}'."
