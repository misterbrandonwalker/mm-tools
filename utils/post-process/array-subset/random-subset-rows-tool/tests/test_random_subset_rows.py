"""Tests for random_subset_rows."""
import sys
from pathlib import Path

from polus.mm.utils.random_subset_rows.random_subset_rows import random_subset_rows

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_random_subset_rows() -> None:
    """Test random_subset_rows."""
    input_file = "rows.txt"
    num_of_samples = 2
    random_seed = 0
    output_file = "output.txt"
    path = Path(__file__).resolve().parent / Path(input_file)
    random_subset_rows(path, num_of_samples, random_seed, output_file)
    assert Path(output_file).exists()


def test_random_subset_rows_cwl() -> None:
    """Test random_subset_rows_cwl."""
    cwl_file = Path("random_subset_rows_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    input_file = "rows.txt"
    input_to_props["input_file"]["path"] = str(
        Path(__file__).resolve().parent / Path(input_file),
    )
    input_to_props["num_of_samples"] = 2
    input_to_props["random_seed"] = 0
    input_to_props["output_file"] = "cwl_output.txt"
    input_yaml_path = Path("random_subset_rows_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path("cwl_output.txt").exists()
