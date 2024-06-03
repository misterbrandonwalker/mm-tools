"""Tests for pose_cluster_filter."""
from pathlib import Path

from polus.mm.utils.pose_cluster_filter.pose_cluster_filter import pose_cluster_filter
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_pose_cluster_filter() -> None:
    """Test pose_cluster_filter."""
    centroid_cutoff = 5
    predicted_poses = [
        "rank2_confidence0.35.sdf",
        "rank3_confidence0.34.sdf",
        "rank1_confidence0.36.sdf",
    ]
    predicted_poses_path = [
        Path(__file__).resolve().parent / Path(pose) for pose in predicted_poses
    ]
    pose_cluster_filter(centroid_cutoff, predicted_poses_path)
    assert Path("filtered_poses.txt").exists()
    with Path("filtered_poses.txt").open() as file:
        lines = file.readlines()
        line_split = lines[0].split()
        indices = [int(index) for index in line_split]
    assert indices == [2, 0]


def test_pose_cluster_filter_cwl() -> None:
    """Test the pose_cluster_filter CWL."""
    cwl_file_str = "pose_cluster_filter_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    predicted_poses = [
        "rank2_confidence0.35.sdf",
        "rank3_confidence0.34.sdf",
        "rank1_confidence0.36.sdf",
    ]

    pose_cluster_filter = Step(clt_path=cwl_file)
    pose_cluster_filter.predicted_poses = [
        {
            "format": "edam:format_3814",
            "class": "File",
            "path": str(Path(__file__).resolve().parent / Path(pose)),
        }
        for pose in predicted_poses
    ]
    pose_cluster_filter.centroid_cutoff = 5

    steps = [pose_cluster_filter]
    filename = "pose_cluster_filter"
    viz = Workflow(steps, filename)

    viz.run()

    outdir = Path("outdir")

    # Use rglob to find all .sdf files
    sdf_files = list(outdir.rglob("*.sdf"))

    # Check if any .sdf files were found
    if not sdf_files:
        msg = f"No .sdf files found in '{outdir}'."
        raise FileNotFoundError(msg)
