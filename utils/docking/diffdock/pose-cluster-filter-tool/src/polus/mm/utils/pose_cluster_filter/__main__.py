"""Package entrypoint for the pose_cluster_filter package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.pose_cluster_filter.pose_cluster_filter import pose_cluster_filter

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.pose_cluster_filter.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="pose_cluster_filter.")


@app.command()
def main(
    centroid_cutoff: float = typer.Option(
        ...,
        "--centroid_cutoff",
        help="",
    ),
    predicted_poses: list[Path] = typer.Option(
        ...,
        "--predicted_poses",
        help="",
    ),
) -> None:
    """pose_cluster_filter."""
    logger.info(f"centroid_cutoff: {centroid_cutoff}")
    logger.info(f"predicted_poses: {predicted_poses}")

    pose_cluster_filter(
        centroid_cutoff=centroid_cutoff,
        predicted_poses=predicted_poses,
    )


if __name__ == "__main__":
    app()
