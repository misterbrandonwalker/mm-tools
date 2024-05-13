"""Package entrypoint for the extract_ligand_protein package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.extract_ligand_protein.extract_ligand_protein import (
    extract_all_ligand_protein,
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.extract_ligand_protein.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="extract_ligand_protein.")


@app.command()
def main(
    input_pdb_path: Path = typer.Option(
        ...,
        "--input_pdb_path",
        help="Input pdb file path, Type: string",
    ),
    output_pdb_path: str = typer.Option(
        ...,
        "--output_pdb_path",
        help="Output pdb file path, Type: string",
    ),
    output_pdb_ligand_path: str = typer.Option(
        ...,
        "--output_pdb_ligand_path",
        help="Output pdb ligand file path, Type: string",
    ),
) -> None:
    """extract_ligand_protein."""
    logger.info(f"input_pdb_path: {input_pdb_path}")
    logger.info(f"output_pdb_path: {output_pdb_path}")
    logger.info(f"output_pdb_ligand_path: {output_pdb_ligand_path}")

    extract_all_ligand_protein(
        input_pdb_path=input_pdb_path,
        output_pdb_path=output_pdb_path,
        output_pdb_ligand_path=output_pdb_ligand_path,
    )


if __name__ == "__main__":
    app()
