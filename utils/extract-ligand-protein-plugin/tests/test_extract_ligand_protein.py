"""Tests for extract_ligand_protein."""
from pathlib import Path

from polus.mm.utils.extract_ligand_protein.extract_ligand_protein import (
    extract_single_ligand_protein,
)


def test_extract_single_ligand_protein() -> None:
    """Test extract_single_ligand_protein."""
    # Get the parent directory of the current file
    test_dir = Path(__file__).resolve().parent

    # Use glob to find all PDB files in the same directory
    pdb_files = test_dir.glob("*.pdb")

    # Iterate through each PDB file and test extract_single_ligand_protein
    for pdb_file in pdb_files:
        pdb = Path(pdb_file)
        output_pdb_path = Path(f"{pdb.stem}_protein.pdb")
        output_pdb_ligand_path = Path(f"{pdb.stem}_ligand.pdb")
        extract_single_ligand_protein(pdb, output_pdb_path, output_pdb_ligand_path)
        with output_pdb_path.open() as f:
            for line in f:
                assert not line.startswith("HETATM")

        with output_pdb_ligand_path.open() as f:
            for line in f:
                assert not line.startswith("ATOM")
