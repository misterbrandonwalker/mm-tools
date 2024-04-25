"""Package entrypoint for the rank_diffdock_poses package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.rank_diffdock_poses.rank_diffdock_poses import rank_diffdock_poses

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.rank_diffdock_poses.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="rank_diffdock_poses.")


@app.command()
def main(
    diffdock_poses: list[Path] = typer.Option(
        ...,
        "--diffdock_poses",
        help="",
    ),
    top_n_confident: int = typer.Option(
        ...,
        "--top_n_confident",
        help="",
    ),
    top_percent_confidence: int = typer.Option(
        ...,
        "--top_percent_confidence",
        help="",
    ),
) -> None:
    """rank_diffdock_poses."""
    logger.info(f"diffdock_poses: {diffdock_poses}")
    logger.info(f"top_n_confident: {top_n_confident}")
    logger.info(f"top_percent_confidence: {top_percent_confidence}")

    rank_diffdock_poses(
        diffdock_poses=diffdock_poses,
        top_n_confident=top_n_confident,
        top_percent_confidence=top_percent_confidence,
    )


if __name__ == "__main__":
    app()
