"""Package entrypoint for the scatter_plot package."""

# Base packages
import logging
from os import environ

import typer
from polus.mm.utils.scatter_plot.scatter_plot import scatter_plot

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.scatter_plot.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="scatter_plot.")


@app.command()
def main(
    xs: list[float] = typer.Option(
        ...,
        "--xs",
        help="",
    ),
    ys: list[float] = typer.Option(
        ...,
        "--ys",
        help="",
    ),
    ys2: list[float] = typer.Option(
        None,
        "--ys2",
        help="",
    ),
    output_png_path: str = typer.Option(
        ...,
        "--output_png_path",
        help="Path to the output png file",
    ),
) -> None:
    """scatter_plot."""
    logger.info(f"xs: {xs}")
    logger.info(f"ys: {ys}")
    logger.info(f"ys2: {ys2}")
    logger.info(f"output_png_path: {output_png_path}")

    scatter_plot(xs=xs, ys=ys, ys2=ys2, output_png_path=output_png_path)


if __name__ == "__main__":
    app()
