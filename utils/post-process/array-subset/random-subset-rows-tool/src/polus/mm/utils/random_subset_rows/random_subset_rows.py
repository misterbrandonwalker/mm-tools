"""Randomly select a subset of rows from a file."""
import random
from pathlib import Path


def random_subset_rows(
    input_file: Path,
    num_of_samples: int,
    random_seed: int,
    output_file: str,
) -> list[int]:
    """random_subset_rows.

    Args:
        input_file:  Path to the input file
        num_of_samples: The number of samples to be selected
        random_seed: The random seed
        output_file: Path to the output file
    Returns:
        List of indices in the random subset
    """
    with input_file.open(mode="r", encoding="utf-8") as f:
        numlines = len(f.readlines())
    indices = list(range(numlines))

    random.seed(random_seed)
    subset: list[int] = random.sample(indices, num_of_samples)

    with Path(output_file).open(mode="w", encoding="utf-8") as f:
        for i in subset[:-1]:
            f.write(f"{i}\n")
        f.write(f"{subset[-1]}")

    return subset
