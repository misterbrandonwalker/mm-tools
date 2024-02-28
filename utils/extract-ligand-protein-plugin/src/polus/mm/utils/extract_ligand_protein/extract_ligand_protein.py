"""Extract ligand and protein from the PDB file."""

from pathlib import Path

import MDAnalysis


def extract_single_ligand_protein(  # noqa: PLR0912
    input_pdb_path: Path,
    output_pdb_path: Path,
    output_pdb_ligand_path: Path,
) -> None:
    """Extract ligand & protein from the PDB file.

    Args:
        input_pdb_path (Path): The path to the input pdb file
        output_pdb_path (Path): The path to the output pdb file
        output_pdb_ligand_path (Path): The path to the output pdb ligand file
    """
    # Load the PDB file
    u = MDAnalysis.Universe(input_pdb_path)

    # Get unique residue names
    protein_atoms = u.select_atoms("protein")  # use simple atom selection when possible

    # Create a new Universe with only protein atoms
    protein_u = MDAnalysis.Universe.empty(
        n_atoms=protein_atoms.n_atoms,
        trajectory=True,
    )  # needed for coordinates
    protein_u.atoms = protein_atoms

    # duplicate the universe object
    dup_u = MDAnalysis.Universe(input_pdb_path)

    # now do the same for the ligand, not protein and not water or salts
    ligand_atoms = u.select_atoms("not protein")

    try:
        # guess the bonds, since input PDB may not have bonds
        dup_u.atoms.guess_bonds()
    except ValueError:
        # ValueError: vdw radii for types: AS.
        # These can be defined manually using the keyword 'vdwradii'
        print("Error: Could not guess bonds. Check the input PDB file.")  # noqa: T201

    has_bonds = False
    try:
        len(dup_u.atoms.bonds)
        has_bonds = True
    except MDAnalysis.exceptions.NoDataError:
        print("No bonds found in the PDB file.")  # noqa: T201

    # Identify water molecules based on the
    # connectivity pattern (Oxygen bonded to two Hydrogens)
    if has_bonds:
        water_indices = set()
        for atom in dup_u.atoms:  # dont use selection resname == 'HOH',
            # pdb file may have different water residue names
            h_bonds = 2
            if (
                atom.name == "O" and len(atom.bonds) == h_bonds
            ):  # if hydrogens are added
                bonded_atoms_names = {a.name for a in atom.bonded_atoms}
                if bonded_atoms_names == {"H"}:  # Check if both bonds are Hydrogens
                    water_indices.add(atom.index)
                    water_indices.update([a.index for a in atom.bonded_atoms])

        # now want to remove all salts, waters without H
        non_bonded = set()
        for atom in dup_u.atoms:
            if len(atom.bonds) == 0:
                non_bonded.add(atom.index)

        # Remove water by excluding the water indices
        if len(water_indices) > 0:
            water_indices_string = " ".join([str(i) for i in water_indices])
            ligand_atoms = ligand_atoms.select_atoms(
                f"not index {water_indices_string}",
            )

        # Remove non bonded atoms
        if len(non_bonded) > 0:
            non_bonded_string = " ".join([str(i) for i in non_bonded])
            ligand_atoms = ligand_atoms.select_atoms(f"not index {non_bonded_string}")

    ligand_u = MDAnalysis.Universe.empty(
        n_atoms=ligand_atoms.n_atoms,
        trajectory=True,
    )  # needed for coordinates
    ligand_u.atoms = ligand_atoms

    protein_u.atoms.write(str(output_pdb_path))
    if len(ligand_u.atoms) > 0:  # will crash if no ligand atoms
        ligand_u.atoms.write(str(output_pdb_ligand_path))


def extract_all_ligand_protein(input_pdb_path: list[Path], outdir: Path) -> None:
    """extract_ligand_protein.

    Args:
        input_pdb_path: Input pdb file path
        outdir: Output collection.

    Returns:
        None
    """
    for pdb in input_pdb_path:
        output_pdb_path = outdir / f"{pdb.stem}_protein.pdb"
        output_pdb_ligand_path = outdir / f"{pdb.stem}_ligand.pdb"
        extract_single_ligand_protein(
            pdb,
            output_pdb_path,
            output_pdb_ligand_path,
        )
