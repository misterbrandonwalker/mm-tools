"""Package entrypoint for the pose_cluster_filter package."""

# Base packages
import argparse
import logging
from os import environ
from pathlib import Path

from polus.mm.utils.pose_cluster_filter.pose_cluster_filter import pose_cluster_filter

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.pose_cluster_filter.")
logger.setLevel(POLUS_LOG)


def main() -> None:
    """Parse the arguments and call the function."""
    # Create the argument parser
    parser = argparse.ArgumentParser(description="pose_cluster_filter.")

    # Add arguments
    parser.add_argument(
        "--centroid_cutoff",
        type=float,
        required=True,
        help="The cutoff distance for the centroid.",
    )
    parser.add_argument(
        "--predicted_poses",
        type=Path,
        nargs="+",
        required=True,
        help="A list of paths to the predicted poses.",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Extract arguments
    centroid_cutoff = args.centroid_cutoff
    predicted_poses = args.predicted_poses

    # Log the arguments
    logger.info(f"centroid_cutoff: {centroid_cutoff}")
    logger.info(f"predicted_poses: {predicted_poses}")

    # Call the function with the arguments
    pose_cluster_filter(
        centroid_cutoff=centroid_cutoff,
        predicted_poses=predicted_poses,
    )


if __name__ == "__main__":
    main()
