"""Package entrypoint for the rank_diffdock_poses package."""

# Base packages
import argparse
import logging
from os import environ
from pathlib import Path

from polus.mm.utils.rank_diffdock_poses.rank_diffdock_poses import rank_diffdock_poses

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.rank_diffdock_poses.")
logger.setLevel(POLUS_LOG)


def main() -> None:
    """rank_diffdock_poses."""
    parser = argparse.ArgumentParser(description="rank_diffdock_poses.")
    parser.add_argument(
        "--diffdock_poses",
        nargs="+",
        type=Path,
        required=True,
        help="List of diffdock pose paths.",
    )
    parser.add_argument(
        "--top_n_confident",
        type=int,
        required=True,
        help="Top N confident poses.",
    )
    parser.add_argument(
        "--top_percent_confidence",
        type=int,
        required=True,
        help="Top percent confidence threshold.",
    )

    args = parser.parse_args()

    logger.info(f"diffdock_poses: {args.diffdock_poses}")
    logger.info(f"top_n_confident: {args.top_n_confident}")
    logger.info(f"top_percent_confidence: {args.top_percent_confidence}")

    rank_diffdock_poses(
        diffdock_poses=args.diffdock_poses,
        top_n_confident=args.top_n_confident,
        top_percent_confidence=args.top_percent_confidence,
    )


if __name__ == "__main__":
    main()
