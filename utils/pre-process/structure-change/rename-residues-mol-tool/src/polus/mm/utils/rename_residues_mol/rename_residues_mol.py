"""rename_residues_mol."""
from pathlib import Path


def rename_residues_mol(input_mol2_path: Path, output_mol2_path: str) -> None:
    """rename_residues_mol.

    Args:
        input_mol2_path: Path to the input file
        output_mol2_path: Path to the output file
    Returns:
        None
    """
    with input_mol2_path.open(encoding="utf-8") as f:
        lines = f.readlines()

    lines_new = []
    index = 7  # mol2 file format residue name column index
    for line in lines:
        this_line = line
        words = this_line.split()
        if len(words) >= index:  # TODO: and only for ATOM records
            this_line = this_line.replace(words[index], "MOL")

        lines_new.append(this_line)

    with Path(output_mol2_path).open(mode="w", encoding="utf-8") as f:
        f.writelines(lines_new)
