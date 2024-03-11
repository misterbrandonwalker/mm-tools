"""Tests for torchdrug_download."""
from pathlib import Path

from polus.mm.utils.torchdrug_download.torchdrug_download import torchdrug_download
from torchdrug import datasets


def test_torchdrug_download_check() -> None:
    """Test torchdrug_download."""
    dataset = "Tox21"
    outdir = Path.cwd()
    dataset_mapping = {"Tox21": datasets.Tox21}
    torchdrug_download(dataset, outdir, dataset_mapping)
    assert Path("tox21.csv").exists()
