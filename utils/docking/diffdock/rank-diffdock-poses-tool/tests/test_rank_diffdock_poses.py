"""Tests for rank_diffdock_poses."""
from pathlib import Path

from polus.mm.utils.rank_diffdock_poses.rank_diffdock_poses import rank_diffdock_poses
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_rank_diffdock_poses() -> None:
    """Test rank_diffdock_poses."""
    diffdock_poses = [
        "rank2_confidence0.35.sdf",
        "rank3_confidence0.34.sdf",
        "rank1_confidence0.36.sdf",
    ]
    top_n_confident = 1000
    top_percent_confidence = 100
    rank_diffdock_poses(diffdock_poses, top_n_confident, top_percent_confidence)
    assert Path("ranked_poses.txt").exists()

    # parse the files, read the order
    with Path("ranked_poses.txt").open() as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    # check the order is 0,1,2
    assert lines == ["2", "0", "1"]


def test_rank_diffdock_poses_cwl() -> None:
    """Test rank_diffdock_poses CWL."""
    if Path("ranked_poses.txt").exists():
        Path("ranked_poses.txt").unlink()

    cwl_file = Path(__file__).resolve().parent.parent / Path(
        "rank_diffdock_poses_0@1@0.cwl",
    )

    rank_diffdock_poses_step = Step(clt_path=cwl_file)
    diffdock_poses = [
        str(Path(__file__).resolve().parent / Path("rank2_confidence0.35.sdf")),
        str(Path(__file__).resolve().parent / Path("rank3_confidence0.34.sdf")),
        str(Path(__file__).resolve().parent / Path("rank1_confidence0.36.sdf")),
    ]

    rank_diffdock_poses_step.diffdock_poses = list(diffdock_poses)
    rank_diffdock_poses_step.top_n_confident = 1000
    rank_diffdock_poses_step.top_percent_confidence = 100

    steps = [rank_diffdock_poses_step]
    filename = "rank_diffdock_poses"
    workflow = Workflow(steps, filename)

    workflow.run()
