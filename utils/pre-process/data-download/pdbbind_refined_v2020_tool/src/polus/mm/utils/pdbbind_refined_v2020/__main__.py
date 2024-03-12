"""Package entrypoint for the pdbbind_refined_v2020 package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.pdbbind_refined_v2020.pdbbind_refined_v2020 import (
    pdbbind_refined_v2020,
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.pdbbind_refined_v2020.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="pdbbind_refined_v2020.")


@app.command()
def main(  # noqa: PLR0913
    output_txt_path: str = typer.Option(
        "system.log",
        "--output_txt_path",
        help="Path to the text dataset file",
    ),
    index_file_name: str = typer.Option(
        "INDEX_refined_data.2020",
        "--index_file_name",
        help="",
    ),
    query: str = typer.Option(
        ...,
        "--query",
        help="query str to search the dataset.",
    ),
    min_row: int = typer.Option(
        1,
        "--min_row",
        help="The row min inex, Type: int",
    ),
    max_row: int = typer.Option(
        ...,
        "--max_row",
        help="The row max inex, Type: int",
    ),
    convert_kd_dg: bool = typer.Option(
        False,
        "--convert_Kd_dG",
        help="If this is set to true, dG will be calculated",
    ),
) -> None:
    """pdbbind_refined_v2020."""
    logger.info(f"output_txt_path: {output_txt_path}")
    logger.info(f"index_file_name: {index_file_name}")
    logger.info(f"query: {query}")
    logger.info(f"min_row: {min_row}")
    logger.info(f"max_row: {max_row}")
    logger.info(f"convert_Kd_dG: {convert_kd_dg}")
    base_dir = "/refined-set"
    Path(base_dir)
    pdbbind_refined_v2020(
        output_txt_path,
        index_file_name,
        base_dir,
        query,
        min_row,
        max_row,
        convert_kd_dg,
    )


if __name__ == "__main__":
    app()
