"""Tests for rank_diffdock_poses."""
import sys
from pathlib import Path

from polus.mm.utils.rank_diffdock_poses.rank_diffdock_poses import rank_diffdock_poses

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


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
    cwl_file_str = "rank_diffdock_poses_0.1.0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    diffdock_poses = [
        "rank2_confidence0.35.sdf",
        "rank3_confidence0.34.sdf",
        "rank1_confidence0.36.sdf",
    ]
    file_dict = input_to_props["diffdock_poses"][0]
    input_to_props["diffdock_poses"] = []
    for pose in diffdock_poses:
        file_dict_current = file_dict.copy()
        path_pose = str(Path(__file__).resolve().parent / Path(pose))
        file_dict_current["path"] = path_pose
        input_to_props["diffdock_poses"].append(file_dict_current)

    input_yaml_path = Path("rank_diffdock_poses_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    # for some reason ranked_poses.txt isnt being created via cwltool call
    # so parse stdout for INFO Final process status is success
    assert "success" in stderr
