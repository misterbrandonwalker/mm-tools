"""Package entrypoint for the combine_structure package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.combine_structure.combine_structure import combine_structure

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.combine_structure.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="combine_structure.")


@app.command()
def main(
    input_structure1: Path = typer.Option(
        ...,
        "--input_structure1",
        help="Input structure 1 file path, Accepted formats: xyz",
    ),
    input_structure2: Path = typer.Option(
        ...,
        "--input_structure2",
        help="Input structure 2 file path, Accepted formats: xyz",
    ),
    output_structure_path: str = typer.Option(
        ...,
        "--output_structure_path",
        help="Output combined PDB file path, Type: string, Accepted formats: pdb",
    ),
) -> None:
    """combine_structure."""
    logger.info(f"input_structure1: {input_structure1}")
    logger.info(f"input_structure2: {input_structure2}")
    logger.info(f"output_structure_path: {output_structure_path}")

    combine_structure(
        input_structure1=input_structure1,
        input_structure2=input_structure2,
        output_structure_path=output_structure_path,
    )


if __name__ == "__main__":
    app()
