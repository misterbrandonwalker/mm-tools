"""Tests for config_tag_mdp."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_config_tag_mdp() -> None:
    """Test config_tag_mdp."""
    cwl_file_str = "config_tag_mdp.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    input_to_props["nsteps"] = 10000
    input_to_props["dt"] = 0.02
    input_to_props["ref-t"] = 298.0
    input_to_props["ref-p"] = 1.0
    input_to_props[
        "config"
    ] = '{"mdp": {"integrator": "md", "rvdw": 1.0, "rcoulomb": 1.0, "coulombtype": \
        "PME", "tc-grps": "system", "tau-t": 2, "constraints": "h-bonds", "nstxout": \
        1000, "nstenergy": 1000, "pcoupl": "Parrinello-Rahman", "tau-p": 1,\
        "compressibility": 4.5e-5, "comm-mode": "Linear", "comm-grps": "system"}}'

    input_yaml_path = Path("config_tag_mdp.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)

    assert "output_config_string" in stdout
