"""Tests for pose_cluster_filter."""
import sys
from pathlib import Path

from polus.mm.utils.pose_cluster_filter.pose_cluster_filter import pose_cluster_filter

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


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
    cwl_file = Path("pose_cluster_filter_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    predicted_poses = [
        "rank2_confidence0.35.sdf",
        "rank3_confidence0.34.sdf",
        "rank1_confidence0.36.sdf",
    ]
    file_dict = input_to_props["predicted_poses"][0]
    input_to_props["predicted_poses"] = []
    for pose in predicted_poses:
        file_dict_current = file_dict.copy()
        path_pose = str(Path(__file__).resolve().parent / Path(pose))
        file_dict_current["path"] = path_pose
        input_to_props["predicted_poses"].append(file_dict_current)

    input_yaml_path = Path("pose_cluster_filter_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert "success" in stderr
