"""Tests for scatter_plot."""
from pathlib import Path

from polus.mm.utils.scatter_plot.scatter_plot import scatter_plot
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_scatter_plot() -> None:
    """Test scatter_plot."""
    scatter_plot([1, 2, 3], [1, 2, 3], [], "test.png")
    assert Path("test.png").exists()


def test_duplicate() -> None:
    """Test scatter plot CWL."""
    cwl_file_str = "scatter_plot_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    scatter_plot = Step(clt_path=cwl_file)
    scatter_plot.xs = [1, 2, 3]
    scatter_plot.ys = [1, 2, 3]
    scatter_plot.ys2 = [1, 2, 3]
    scatter_plot.output_png_path = "test.png"

    steps = [scatter_plot]
    filename = "scatter_plot"
    viz = Workflow(steps, filename)

    viz.run()

    outdir = Path("outdir")
    files = list(outdir.rglob("test.png"))

    assert (
        files
    ), f"The file 'test.png' does not exist in any subdirectory of '{outdir}'."
