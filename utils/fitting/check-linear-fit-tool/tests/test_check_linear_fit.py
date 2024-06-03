"""Tests for check_linear_fit."""
from pathlib import Path

from polus.mm.utils.check_linear_fit.check_linear_fit import check_linear_fit
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_check_linear_fit() -> None:
    """Test check_linear_fit."""
    xs = [1.0, 2.0, 3.0]
    ys = [1.0, 2.0, 3.0]
    tol_quad = 0.1
    slope_min = 0.5
    slope_max = 1.5
    is_within_bounds = check_linear_fit(xs, ys, tol_quad, slope_min, slope_max)
    assert is_within_bounds


# now check for case that is out of bounds, make ys very large
def test_check_linear_fit_out_of_bounds() -> None:
    """Test check_linear_fit."""
    xs = [1.0, 2.0, 3.0]
    ys = [-5, 720, 100.0]
    tol_quad = 0.1
    slope_min = 0.5
    slope_max = 1.0
    is_within_bounds = check_linear_fit(xs, ys, tol_quad, slope_min, slope_max)
    assert not is_within_bounds


def test_check_linear_fit_cwl() -> None:
    """Test check_linear_fit CWL."""
    # Define the input parameters
    xs = [1.0, 2.0, 3.0]
    ys = [1.0, 2.0, 3.0]
    tol_quad = 0.1
    slope_min = 0.5
    slope_max = 1.5

    # Define paths
    cwl_file_str = "check_linear_fit_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    # Create the CWL step
    check_linear_fit_step = Step(clt_path=cwl_file)
    check_linear_fit_step.xs = xs
    check_linear_fit_step.ys = ys
    check_linear_fit_step.tol_quad = tol_quad
    check_linear_fit_step.slope_min = slope_min
    check_linear_fit_step.slope_max = slope_max

    # Create the workflow and run it
    steps = [check_linear_fit_step]
    filename = "check_linear_fit_workflow"
    workflow = Workflow(steps, filename)
    workflow.run()

    # cant check output because it is a boolean and no way to capture stdout
