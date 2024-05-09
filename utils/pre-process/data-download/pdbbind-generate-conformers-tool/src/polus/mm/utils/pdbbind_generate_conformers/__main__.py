"""Package entrypoint for the pdbbind_generate_conformers package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.pdbbind_generate_conformers.pdbbind_generate_conformers import (
    pdbbind_generate_conformers,
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.pdbbind_generate_conformers.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="pdbbind_generate_conformers.")


@app.command()
def main(  # noqa: PLR0913
    input_excel_path: Path = typer.Option(
        ...,
        "--input_excel_path",
        help="",
    ),
    query: str = typer.Option(
        ...,
        "--query",
        help="query str to search the dataset",
    ),
    output_txt_path: str = typer.Option(
        ...,
        "--output_txt_path",
        help="Path to the text dataset file",
    ),
    min_row: int = typer.Option(
        ...,
        "--min_row",
        help="The row min inex, Type int",
    ),
    max_row: int = typer.Option(
        ...,
        "--max_row",
        help="The row max inex, Type int",
    ),
    smiles_column: str = typer.Option(
        ...,
        "--smiles_column",
        help="The name of the smiles column",
    ),
    binding_data_column: str = typer.Option(
        ...,
        "--binding_data_column",
        help="The name of the binding data column",
    ),
    convert_kd_dg: bool = typer.Option(
        ...,
        "--convert_kd_dg",
        help="If this is set to true, dG will be calculated",
    ),
) -> None:
    """pdbbind_generate_conformers."""
    logger.info(f"input_excel_path: {input_excel_path}")
    logger.info(f"query: {query}")
    logger.info(f"output_txt_path: {output_txt_path}")
    logger.info(f"min_row: {min_row}")
    logger.info(f"max_row: {max_row}")
    logger.info(f"smiles_column: {smiles_column}")
    logger.info(f"binding_data_column: {binding_data_column}")
    logger.info(f"convert_kd_dg: {convert_kd_dg}")

    pdbbind_generate_conformers(
        input_excel_path=input_excel_path,
        query=query,
        output_txt_path=output_txt_path,
        min_row=min_row,
        max_row=max_row,
        smiles_column=smiles_column,
        binding_data_column=binding_data_column,
        convert_kd_dg=convert_kd_dg,
    )


if __name__ == "__main__":
    app()
