"""Pose Cluster Filter Plugin."""
import re
from pathlib import Path

import numpy as np
from rdkit import Chem
from rdkit.Chem import rdMolTransforms
from rdkit.ML.Cluster import Butina


def euclidean_dist(pi: Chem.SDMolSupplier, pj: Chem.SDMolSupplier) -> float:
    """Compute the Euclidean distance between two input molecule centroids.

    Args:
        pi (Chem.SDMolSupplier): the ith molecule
        pj (Chem.SDMolSupplier): the jth molecule

    Returns:
        float: distance between two input molecule centroids
    """
    # GetConformers will just use input
    # coordinates if conformations are not pre-generated
    confi = pi.GetConformers()[0]
    confj = pj.GetConformers()[0]
    centeri = rdMolTransforms.ComputeCentroid(
        confi,
    )  # pylint: disable=c-extension-no-member
    centerj = rdMolTransforms.ComputeCentroid(
        confj,
    )  # pylint: disable=c-extension-no-member
    dv = np.array([centeri.x, centeri.y, centeri.z]) - np.array(
        [centerj.x, centerj.y, centerj.z],
    )
    return float(np.sqrt(np.dot(dv, dv)))


def parse_confidence(file_name: str) -> float:
    """This function returns the confidence score from a filename.

    Filenames must follow the format 'rankX_confidenceY.mol',
    where X is a positive integer and Y is a float.
    This format is the default for DiffDock outputs.".

    Args:
        file_name (str): The filename of output pose

    Returns:
        float: The confidence value from pose
    """
    return float(re.findall("rank[0-9]+_confidence(.*).sdf", file_name)[0])


def pose_cluster_filter(centroid_cutoff: float, predicted_poses: list[Path]) -> None:
    """pose_cluster_filter.

    Args:
        centroid_cutoff: The cutoff distance for clustering poses
        predicted_poses: The list of poses to be filtered
    Returns:
        None
    """
    # sanitize flag is still left True (default value),
    # set removeHs to False to keep hydrogens
    pred_mols = [
        Chem.SDMolSupplier(pose, removeHs=False)[0] for pose in predicted_poses
    ]
    if (
        None in pred_mols
    ):  # unreproducible failure rdkit returned None in virtual screen
        msg = "Rdkit failed to read one of the poses"
        raise ValueError(msg)
    predicted_poses_str = [pose.name for pose in predicted_poses]

    # Cluster a pose into group of other
    # poses via centroid distance if beneath threshold
    true_poses = []
    index_to_cluster_index = {}
    clusters = Butina.ClusterData(
        pred_mols,
        len(pred_mols),
        centroid_cutoff,
        distFunc=euclidean_dist,
    )
    for cluster_index, cluster in enumerate(clusters):
        names = [predicted_poses_str[index] for index in cluster]
        confidences = [parse_confidence(name) for name in names]
        max_confidence = max(confidences)
        confidence_to_indices = dict(zip(confidences, cluster))
        max_index = confidence_to_indices[max_confidence]
        true_poses.append(max_index)
        index_to_cluster_index[max_index] = cluster_index

    # save pose index and cluster index to filtered_filename
    lines = [f"{index} {index_to_cluster_index[index]} \n" for index in true_poses]
    with Path("filtered_poses.txt").open(mode="w", encoding="utf-8") as file:
        file.writelines(lines)
