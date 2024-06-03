"""Package entrypoint for the random_subset_rows package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.random_subset_rows.random_subset_rows import random_subset_rows

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.random_subset_rows.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="random_subset_rows.")


@app.command()
def main(
    input_file: Path = typer.Option(
        ...,
        "--input_file",
        help="",
    ),
    num_of_samples: int = typer.Option(
        ...,
        "--num_of_samples",
        help="",
    ),
    random_seed: int = typer.Option(
        ...,
        "--random_seed",
        help="",
    ),
    output_file: str = typer.Option(
        ...,
        "--output_file",
        help="",
    ),
) -> None:
    """random_subset_rows."""
    logger.info(f"input_file: {input_file}")
    logger.info(f"num_of_samples: {num_of_samples}")
    logger.info(f"random_seed: {random_seed}")
    logger.info(f"output_file: {output_file}")

    random_subset_rows(
        input_file=input_file,
        num_of_samples=num_of_samples,
        random_seed=random_seed,
        output_file=output_file,
    )


if __name__ == "__main__":
    app()
