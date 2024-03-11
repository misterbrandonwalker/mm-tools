"""torchdrug_download."""
from pathlib import Path


def torchdrug_download(dataset: str, outdir: Path, dataset_mapping: dict) -> None:
    """torchdrug.

    Args:
        dataset: Input dataset to extract
        outdir: Output collection.
        dataset_mapping: Mapping of dataset to class.

    Returns:
        None
    """
    # Create an instance of the selected dataset class
    selected_dataset_class = dataset_mapping[dataset]
    # lazy = False causes issues with PDBBind dataset such as invalid sequence
    dataset = selected_dataset_class(outdir, lazy=True)
