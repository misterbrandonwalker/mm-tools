"""Package entrypoint for the sanitize_ligand package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import filepattern as fp
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
    pattern: str = typer.Option(
        ...,
        "--pattern",
        help="Input filepattern to be processed.",
    ),
    in_dir: Path = typer.Option(
        ...,
        "--indir",
        help="Input directory.",
        exists=True,
        writable=True,
        file_okay=False,
        resolve_path=True,
    ),
    out_dir: Path = typer.Option(
        ...,
        "--outdir",
        help="Output directory.",
        exists=True,
        writable=True,
        file_okay=False,
        resolve_path=True,
    ),
) -> None:
    """Sanitize Ligand."""
    logger.info(f"pattern: {pattern}")
    logger.info(f"indir: {in_dir}")
    logger.info(f"outdir: {out_dir}")
    ligand_file_paths = []
    ligand_files = fp.FilePattern(in_dir, pattern)
    for input_small_mol_ligand in ligand_files():
        ligand = input_small_mol_ligand[-1][0]
        ligand_file_paths.append(ligand)

    sanitize_ligand(ligand_file_paths, out_dir)


if __name__ == "__main__":
    app()
