"""scatter_plot."""
import matplotlib.pyplot as plt


def scatter_plot(
    xs: list[float],
    ys: list[float],
    ys2: list[float],
    output_png_path: str,
) -> None:
    """scatter_plot.

    Args:
        xs: X values
        ys: Y values
        ys2: Special case Y value
        output_png_path: Path to the output png file

    Returns:
        None
    """
    plt.scatter(xs, ys)
    if ys2 != []:
        plt.scatter(xs, ys2)

    plt.savefig(output_png_path)
