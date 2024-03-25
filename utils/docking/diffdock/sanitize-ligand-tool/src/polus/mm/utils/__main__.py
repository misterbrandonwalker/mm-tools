"""Package entrypoint for the sanitize_ligand package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.sanitize_ligand import sanitize_ligand

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.sanitize_ligand")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="Sanitize Ligand.")


@app.command()
def main(
    input_small_mol_ligand: Path = typer.Option(
        ...,
        "--input_small_mol_ligand",
        help="Input input_small_mol_ligand to be processed.",
    ),
) -> None:
    """Sanitize Ligand."""
    logger.info(f"input_small_mol_ligand: {input_small_mol_ligand}")
    sanitize_ligand(input_small_mol_ligand)


if __name__ == "__main__":
    app()
