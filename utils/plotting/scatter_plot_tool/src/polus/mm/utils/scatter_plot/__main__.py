"""parse arguments and call scatter_plot."""
import argparse
import logging
from os import environ

from polus.mm.utils.scatter_plot.scatter_plot import scatter_plot

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.scatter_plot.")
logger.setLevel(POLUS_LOG)


def main(xs: list, ys: list, ys2: list, output_png_path: str) -> None:
    """scatter_plot."""
    logger.info(f"xs: {xs}")
    logger.info(f"ys: {ys}")
    logger.info(f"ys2: {ys2}")
    logger.info(f"output_png_path: {output_png_path}")

    scatter_plot(xs=xs, ys=ys, ys2=ys2, output_png_path=output_png_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="scatter_plot")
    parser.add_argument(
        "--xs",
        type=float,
        nargs="+",
        required=True,
        help="List of x values",
    )
    parser.add_argument(
        "--ys",
        type=float,
        nargs="+",
        required=True,
        help="List of y values",
    )
    parser.add_argument(
        "--ys2",
        type=float,
        nargs="+",
        help="Optional second list of y values",
    )
    parser.add_argument(
        "--output_png_path",
        type=str,
        required=True,
        help="Path to the output \
              png file",
    )

    args = parser.parse_args()

    main(xs=args.xs, ys=args.ys, ys2=args.ys2, output_png_path=args.output_png_path)
