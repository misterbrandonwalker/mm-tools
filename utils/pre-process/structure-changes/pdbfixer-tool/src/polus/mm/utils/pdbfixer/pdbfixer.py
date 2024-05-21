"""PDBFixer plugin."""
from pathlib import Path

import openmm.app as omma

from pdbfixer import PDBFixer  # type: ignore[attr-defined]


def input_pdbfixer(  # noqa: PLR0913
    input_pdb_path: str,
    input_helper_pdb_path: str,
    pdbid: str,
    url: str,
    add_residues: bool,
    replace_nonstandard: bool,
    add_atoms: str,
    keep_heterogens: str,
    output_pdb_path: str,
) -> None:
    """pdbfixer.

    Args:
        input_pdb_path: The input pdb file
        input_helper_pdb_path: The template pdb file
        pdbid: PDB id from RCSB
        url: URL to retrieve PDB from
        add_residues: If set to True, adds missing residue
        replace_nonstandard: Replace nonstandard residues with standard equivalents
        add_atoms: What missing atoms to add, all, heavy or none
        keep_heterogens: What heterogens to keep, all, water or none
        output_pdb_path: The output pdb file path

    Returns:
        None
    """
    if input_pdb_path and not Path.exists(Path(input_pdb_path)):
        msg = f"Can not find file {input_pdb_path}"
        raise FileNotFoundError(msg)

    if input_helper_pdb_path and not Path.exists(Path(input_helper_pdb_path)):
        msg = f"Can not find file {input_helper_pdb_path}"
        raise FileNotFoundError(msg)

    if check_pdb_null(input_pdb_path, pdbid, url):
        msg = f"All the residues in {input_pdb_path} are unkown"
        raise ValueError(msg)

    if (input_pdb_path is None) and (pdbid is None) and (url is None):
        msg = "No input is provided"
        raise ValueError(msg)

    runpdbfixer(
        input_pdb_path,
        input_helper_pdb_path,
        output_pdb_path,
        add_atoms,
        add_residues,
        pdbid,
        url,
        replace_nonstandard,
        keep_heterogens,
    )


def check_pdb_null(input_pdb_path: str, pdbid: str, url: str) -> bool:
    """Check if all of the residues are unknown.

    Args:
        input_pdb_path (str): The input PDB structure path
        pdbid (str): PDB id from RCSB
        url (str): URL to retrieve PDB from
    Returns:
        bool: Return True if all of the residues are unknown
    """
    if input_pdb_path:
        fixer = PDBFixer(filename=input_pdb_path)
    elif pdbid:
        fixer = PDBFixer(pdbid=pdbid)
    elif url:
        fixer = PDBFixer(url=url)

    all_unknown: bool = not [
        residue
        for residue in fixer.topology.residues()
        if residue.name in fixer.templates
    ]

    return all_unknown


def find_missing_residues(fixer: PDBFixer) -> PDBFixer:
    """Find missing residues and add them to the PDBFixer instance.

    Finds the missing residues and adds missing residues within a
    chain to prevent "floppy tails," which can lead to an increase in the box size,
    significantly increasingthe computation time. This step is taken as floppy tails
    are generally not critical for binding.

    Args:
        fixer (PDBFixer): The input PDBFixer instance

    Returns:
        PDBFixer: The output PDBFixer instance with added missing residues
    """
    fixer.findMissingResidues()
    fixer_chains: list[omma.topology.Chain] = list(fixer.topology.chains())
    fixer_chain_res_idx_pairs: list[tuple[int, int]] = list(
        fixer.missingResidues.keys(),
    )
    for chain_idx, res_idx in fixer_chain_res_idx_pairs:
        chain = fixer_chains[chain_idx]
        if res_idx == 0 or res_idx == len(list(chain.residues())):
            del fixer.missingResidues[(chain_idx, res_idx)]

    # Sometimes, protein structures have missing residues, but the type of these
    # missing residues is unknown and denoted as UNK. Figuring out the correct type
    # of these residues is beyond the capabilities of a command-line tool. Therefore,
    # we often remove missing residues without a template, such as UNK, N, and others.
    for key, resnames in list(fixer.missingResidues.items()):
        fixer.missingResidues[key] = [r for r in resnames if r in fixer.templates]
    return fixer


# pylint: disable=too-many-arguments


def runpdbfixer(  # noqa: PLR0913
    input_pdb_path: str,
    input_helper_pdb_path: str,
    output_pdb_path: str,
    add_atoms: str,
    add_res: bool,
    pdbid: str,
    url: str,
    rep_nonstandard: bool,
    heterogens: str,
) -> None:
    """Fixes the protein structure using PDBFixer.

    Fixes the protein structure using PDBFixer.PDBFixer offers options
    to add hydrogens and solvate the system, but in our usage, we employ
    PDBFixer solely for adding missing heavy atoms and residues.

    Args:
        input_pdb_path (str): The input PDB structure path
        output_pdb_path (str): The output PDB structure path
        input_helper_pdb_path (str): The input helper PDB structure path
        add_atoms (str): What missing atoms to add: all, heavy, hydrogen, or none
        add_res (bool): If set to True, adds missing residues
        pdbid (str): PDB id from RCSB
        url (str): URL to retrieve PDB from
        rep_nonstandard (bool): Replace nonstandard residues with standard equivalents
        heterogens (str): What heterogens to keep: all, water, or none
    """
    # The input can be one of these options
    if input_pdb_path:
        fixer = PDBFixer(filename=input_pdb_path)
    elif pdbid:
        fixer = PDBFixer(pdbid=pdbid)
    elif url:
        fixer = PDBFixer(url=url)

    if add_res:
        if input_helper_pdb_path:
            helper_fixer = PDBFixer(filename=input_helper_pdb_path)
            # Finds the missing residues based on the PDBbind structure but uses
            # the sequence info from the helper file
            helper_fixer.topology = fixer.topology
            helper_fixer = find_missing_residues(helper_fixer)
            fixer.missingResidues = helper_fixer.missingResidues
        else:
            fixer = find_missing_residues(fixer)
    else:
        fixer.missingResidues = {}

    if rep_nonstandard:
        fixer.findNonstandardResidues()
        fixer.replaceNonstandardResidues()

    if heterogens == "none":
        fixer.removeHeterogens(False)
    elif heterogens == "water":
        fixer.removeHeterogens(True)

    fixer.findMissingAtoms()
    if add_atoms not in ("all", "heavy"):
        fixer.missingAtoms = {}
        fixer.missingTerminals = {}

    # Adds identified missing atoms and residues
    fixer.addMissingAtoms()
    output_path = Path(output_pdb_path)
    with output_path.open(mode="w", encoding="utf-8") as wfile:
        omma.PDBFile.writeFile(fixer.topology, fixer.positions, wfile, keepIds=True)
