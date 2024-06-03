"""Package entrypoint for the rename_residues_mol package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.rename_residues_mol.rename_residues_mol import rename_residues_mol

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.rename_residues_mol.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="rename_residues_mol.")


@app.command()
def main(
    input_mol2_path: Path = typer.Option(
        ...,
        "--input_mol2_path",
        help="",
    ),
    output_mol2_path: str = typer.Option(
        ...,
        "--output_mol2_path",
        help="Path to the output file",
    ),
) -> None:
    """rename_residues_mol."""
    logger.info(f"input_mol2_path: {input_mol2_path}")
    logger.info(f"output_mol2_path: {output_mol2_path}")

    rename_residues_mol(
        input_mol2_path=input_mol2_path,
        output_mol2_path=output_mol2_path,
    )


if __name__ == "__main__":
    app()
