"""This module ranks the poses from a DiffDock output based on confidence scores."""
import re
from pathlib import Path


def rank_diffdock_poses(
    diffdock_poses: list[Path],
    top_n_confident: int,
    top_percent_confidence: int,
) -> None:
    """rank_diffdock_poses.

    Args:
        diffdock_poses: List of poses from DiffDock output
        top_n_confident: Number of poses to keep based on confidence score
        top_percent_confidence: Percentage of poses to keep based on confidence score
    Returns:
        None
    """
    confidences = [parse_confidence(name) for name in diffdock_poses]
    diffdock_poses_str = [str(name) for name in diffdock_poses]
    confidence_to_pose: dict[float, Path] = dict(zip(confidences, diffdock_poses))
    file_to_index: dict[str, int] = dict(
        zip(diffdock_poses_str, range(len(diffdock_poses))),
    )

    # First filter by absolute value top_n_confident
    # if user only wants to use top_percent_confidence,
    # can set top_n_confident to trivially high number
    # if user only wants to use top_n_confident,
    # then can set top_percent_confidence to 100
    sorted_list = sorted(confidence_to_pose.items(), reverse=True)
    sorted_pose_list = [v for (k, v) in sorted_list]
    poses = sorted_pose_list[:top_n_confident]
    # Next filter by top percentage of confident poses
    num_poses = int(top_percent_confidence * 0.01 * len(poses))
    poses = poses[:num_poses]
    # Write to ranked_filename
    path = Path("ranked_poses.txt")
    with path.open("w", encoding="utf-8") as file:
        file.writelines([f"{file_to_index[str(string)]} \n" for string in poses])


def parse_confidence(file_name: Path) -> float:
    """This function returns the confidence score from a filename.

    Filenames must follow the format 'rankX_confidenceY.mol',
    where X is a positive integer and Y is a float.
    This format is the default for DiffDock outputs.".

    Args:
        file_name (Path): The filename of output pose

    Returns:
        float: The confidence value from pose
    """
    return float(re.findall("rank[0-9]+_confidence(.*).sdf", str(file_name))[0])
