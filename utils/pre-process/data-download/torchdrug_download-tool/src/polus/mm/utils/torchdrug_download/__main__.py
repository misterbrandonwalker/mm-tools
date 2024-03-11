"""Package entrypoint for the torchdrug package."""

# Base packages
import logging
from enum import Enum
from os import environ
from pathlib import Path

import typer
from polus.mm.utils.torchdrug_download.torchdrug_download import torchdrug_download
from torchdrug import datasets

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.torchdrug_download.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="torchdrug_download.")


class DatabaseEnum(str, Enum):
    """class DatabaseEnum for the input database to be processed."""

    ClinTox = "ClinTox"
    PDBBind = "PDBBind"
    FB15k = "FB15k"
    FB15k237 = "FB15k237"
    WN18 = "WN18"
    WN18RR = "WN18RR"
    Hetionet = "Hetionet"
    BACE = "BACE"
    BBBP = "BBBP"
    CEP = "CEP"
    ChEMBLFiltered = "ChEMBLFiltered"
    Delaney = "Delaney"
    FreeSolv = "FreeSolv"
    HIV = "HIV"
    Lipophilicity = "Lipophilicity"
    MUV = "MUV"
    Malaria = "Malaria"
    OPV = "OPV"
    QM8 = "QM8"
    QM9 = "QM9"
    SIDER = "SIDER"
    Tox21 = "Tox21"
    ToxCast = "ToxCast"
    ZINC250k = "ZINC250k"
    ZINC2m = "ZINC2m"
    MOSES = "MOSES"
    PCQM4M = "PCQM4M"
    BetaLactamase = "BetaLactamase"
    Fluorescence = "Fluorescence"
    Stability = "Stability"
    Solubility = "Solubility"
    BinaryLocalization = "BinaryLocalization"
    SubcellularLocalization = "SubcellularLocalization"
    EnzymeCommission = "EnzymeCommission"
    GeneOntology = "GeneOntology"
    AlphaFoldDB = "AlphaFoldDB"
    Fold = "Fold"
    SecondaryStructure = "SecondaryStructure"
    ProteinNet = "ProteinNet"
    HumanPPI = "HumanPPI"
    YeastPPI = "YeastPPI"
    PPIAffinity = "PPIAffinity"
    BindingDB = "BindingDB"
    USPTO50k = "USPTO50k"
    Cora = "Cora"
    PubMed = "PubMed"


@app.command()
def main(
    dataset: DatabaseEnum = typer.Option(
        ...,
        "--dataset",
        help="Input database to be processed.",
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
    """torchdrug_download."""
    dataset_mapping = {
        "PDBBind": datasets.PDBBind,
        "ClinTox": datasets.ClinTox,
        "FB15k": datasets.FB15k,
        "FB15k237": datasets.FB15k237,
        "WN18": datasets.WN18,
        "WN18RR": datasets.WN18RR,
        "Hetionet": datasets.Hetionet,
        "BACE": datasets.BACE,
        "BBBP": datasets.BBBP,
        "CEP": datasets.CEP,
        "ChEMBLFiltered": datasets.ChEMBLFiltered,
        "Delaney": datasets.Delaney,
        "FreeSolv": datasets.FreeSolv,
        "HIV": datasets.HIV,
        "Lipophilicity": datasets.Lipophilicity,
        "MUV": datasets.MUV,
        "Malaria": datasets.Malaria,
        "OPV": datasets.OPV,
        "QM8": datasets.QM8,
        "QM9": datasets.QM9,
        "SIDER": datasets.SIDER,
        "Tox21": datasets.Tox21,
        "ToxCast": datasets.ToxCast,
        "ZINC250k": datasets.ZINC250k,
        "ZINC2m": datasets.ZINC2m,
        "MOSES": datasets.MOSES,
        "PCQM4M": datasets.PCQM4M,
        "BetaLactamase": datasets.BetaLactamase,
        "Fluorescence": datasets.Fluorescence,
        "Stability": datasets.Stability,
        "Solubility": datasets.Solubility,
        "BinaryLocalization": datasets.BinaryLocalization,
        "SubcellularLocalization": datasets.SubcellularLocalization,
        "EnzymeCommission": datasets.EnzymeCommission,
        "GeneOntology": datasets.GeneOntology,
        "AlphaFoldDB": datasets.AlphaFoldDB,
        "Fold": datasets.Fold,
        "SecondaryStructure": datasets.SecondaryStructure,
        "ProteinNet": datasets.ProteinNet,
        "HumanPPI": datasets.HumanPPI,
        "YeastPPI": datasets.YeastPPI,
        "PPIAffinity": datasets.PPIAffinity,
        "BindingDB": datasets.BindingDB,
        "USPTO50k": datasets.USPTO50k,
        "Cora": datasets.Cora,
        "PubMed": datasets.PubMed,
    }

    if dataset not in dataset_mapping:
        msg = f"Unsupported dataset: {dataset}"
        raise ValueError(msg)

    logger.info(f"database: {dataset}")
    logger.info(f"outdir: {out_dir}")
    torchdrug_download(dataset, out_dir, dataset_mapping)


if __name__ == "__main__":
    app()
