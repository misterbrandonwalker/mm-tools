"""Combine two structures into a single PDB file using RDKit."""
from pathlib import Path
from typing import Optional

from rdkit import Chem


def combine_structure(
    input_structure1: Path,
    input_structure2: Path,
    output_structure_path: str,
) -> None:
    """combine_structure.

    Args:
        input_structure1: Input structure 1 file path, Accepted formats: xyz
        input_structure2: Input structure 2 file path, Accepted formats: xyz
        output_structure_path: Output combined PDB file path, Accepted formats: pdb
    Returns:
        None
    """
    combine_structure_rdkit(input_structure1, input_structure2, output_structure_path)


def read_xyz_rdkit(
    input_structure_path: Path,
) -> Optional[Chem.rdchem.Mol]:  # pylint: disable=c-extension-no-member
    """Read a PDB file using RDKit.

    Args:
        input_structure_path (Path): The path to the xyz structure

    Returns:
        Optional[Chem.rdchem.Mol]: The created molecule object
    """
    xyz = Chem.rdmolfiles.MolFromXYZFile(
        str(input_structure_path),
    )  # pylint: disable=c-extension-no-member
    if not xyz:
        print(  # noqa: T201
            f"Error: failed to generate molecule from file {input_structure_path}",
        )
        return None

    return xyz


def combine_structure_rdkit(
    input_structure1_path: Path,
    input_structure2_path: Path,
    output_structure_path: str,
) -> None:
    """Combine two structures into a single PDB file using RDKit.

    Args:
        input_structure1_path (Path): The path to the xyz structure 1
        input_structure2_path (Path): The path to the xyz structure 2
        output_structure_path (str): The path to the output combined structure
    """
    structure1 = read_xyz_rdkit(input_structure1_path)
    structure2 = read_xyz_rdkit(input_structure2_path)

    if structure1 and structure2:
        combo = Chem.CombineMols(structure1, structure2)  # pylint: disable=no-member
        with Chem.PDBWriter(
            output_structure_path,
        ) as writer:  # pylint: disable=no-member
            writer.write(combo)
