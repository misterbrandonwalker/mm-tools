"""Package entrypoint for the pdbfixer package."""

# Base packages
import logging
from os import environ

import typer
from polus.mm.utils.pdbfixer.pdbfixer import input_pdbfixer

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.pdbfixer.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="pdbfixer.")


@app.command()
def main(  # noqa: PLR0913
    input_pdb_path: str = typer.Option(
        ...,
        "--input_pdb_path",
        help="",
    ),
    input_helper_pdb_path: str = typer.Option(
        ...,
        "--input_helper_pdb_path",
        help="",
    ),
    pdbid: str = typer.Option(
        "",
        "--pdbid",
        help="PDB id from RCSB",
    ),
    url: str = typer.Option(
        "",
        "--url",
        help="URL to retrieve PDB from",
    ),
    add_residues: bool = typer.Option(
        False,
        "--add_residues",
        help="If set to True, adds missing residue",
    ),
    replace_nonstandard: bool = typer.Option(
        False,
        "--replace_nonstandard",
        help="Replace nonstandard residues with standard equivalents",
    ),
    add_atoms: str = typer.Option(
        "all",
        "--add_atoms",
        help="What missing atoms to add, all, heavy or none",
    ),
    keep_heterogens: str = typer.Option(
        "all",
        "--keep_heterogens",
        help="What heterogens to keep, all, water or none ",
    ),
    output_pdb_path: str = typer.Option(
        ...,
        "--output_pdb_path",
        help="Output pdb file path.",
    ),
) -> None:
    """pdbfixer."""
    output_pdb_path = str(output_pdb_path)
    logger.info(f"input_pdb_path_pattern: {input_pdb_path}")
    logger.info(f"input_helper_pdb_path_pattern: {input_helper_pdb_path}")
    logger.info(f"pdbid: {pdbid}")
    logger.info(f"url: {url}")
    logger.info(f"add_residues: {add_residues}")
    logger.info(f"replace_nonstandard: {replace_nonstandard}")
    logger.info(f"add_atoms: {add_atoms}")
    logger.info(f"keep_heterogens: {keep_heterogens}")
    logger.info(f"output_pdb_path: {output_pdb_path}")
    input_pdbfixer(
        input_pdb_path,
        input_helper_pdb_path,
        pdbid,
        url,
        add_residues,
        replace_nonstandard,
        add_atoms,
        keep_heterogens,
        output_pdb_path,
    )


if __name__ == "__main__":
    app()
