"""Tests for config_tag_mdp."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_config_tag_mdp() -> None:
    """Test config_tag_mdp."""
    # Define paths and input properties
    cwl_file_str = "config_tag_mdp_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_props = {
        "nsteps": 10000,
        "dt": 0.02,
        "ref-t": 298.0,
        "ref-p": 1.0,
        "config": '{"mdp": {"integrator": "md", "rvdw": 1.0, \
            "rcoulomb": 1.0, "coulombtype": \
                    "PME", "tc-grps": "system", \
                        "tau-t": 2, "constraints": \
                            "h-bonds", "nstxout": \
                    1000, "nstenergy": 1000, "pcoupl": \
                        "Parrinello-Rahman", "tau-p": 1, \
                    "compressibility": 4.5e-5, "comm-mode": \
                        "Linear", "comm-grps": "system"}}',
    }

    # Create the CWL step
    config_tag_mdp_step = Step(clt_path=cwl_file)
    config_tag_mdp_step.nsteps = input_props["nsteps"]
    config_tag_mdp_step.dt = input_props["dt"]
    config_tag_mdp_step.ref_t = input_props["ref-t"]
    config_tag_mdp_step.ref_p = input_props["ref-p"]
    config_tag_mdp_step.config = input_props["config"]

    # Create the workflow and run it
    steps = [config_tag_mdp_step]
    filename = "config_tag_mdp_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()
