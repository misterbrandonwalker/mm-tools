"""Tests for scatter_plot."""
import sys
from pathlib import Path

from polus.mm.utils.scatter_plot.scatter_plot import scatter_plot

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_scatter_plot() -> None:
    """Test scatter_plot."""
    scatter_plot([1, 2, 3], [1, 2, 3], [], "test.png")
    assert Path("test.png").exists()


def test_duplicate() -> None:
    """Test pdb."""
    cwl_file_str = "scatter_plot_0.1.0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["xs"] = [1, 2, 3]
    input_to_props["ys"] = [1, 2, 3]
    input_to_props["output_png_path"] = "test.png"
    input_yaml_path = Path("scatter_plot_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    call_cwltool(cwl_file, input_yaml_path)
    assert Path("test.png").exists()
