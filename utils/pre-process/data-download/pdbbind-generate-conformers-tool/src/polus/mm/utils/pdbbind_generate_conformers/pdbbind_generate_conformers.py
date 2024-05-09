"""Generate conformers for a dataset of ligands and binding data."""
import math
from pathlib import Path

import pandas
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem


def pdbbind_generate_conformers(  # noqa: PLR0913
    input_excel_path: Path,
    query: str,
    output_txt_path: str,
    min_row: int,
    max_row: int,
    smiles_column: str,
    binding_data_column: str,
    convert_kd_dg: bool,
) -> None:
    """pdbbind_generate_conformers.

    Args:
        input_excel_path: Path to the input xlsx file
        query: query str to search the dataset
        output_txt_path: Path to the text dataset file
        min_row: The row min index
        max_row: The row max index
        smiles_column: The name of the smiles column
        binding_data_column: The name of the binding data column
        convert_kd_dg: If this is set to true, dG will be calculated
    Returns:
        None
    """
    load_data(
        input_excel_path,
        query,
        smiles_column,
        binding_data_column,
        output_txt_path,
        min_row,
        max_row,
        convert_kd_dg,
    )


def calculate_dg(kd: float) -> float:
    """Calculates binding free energy from kd, See https://en.wikipedia.org/wiki/Binding_constant.

    Args:
        kd (float): The binding affinity of the protein-ligand complex

    Returns:
        float: The binding free energy
    """
    # Calculate the binding free energy from kd so we can make the correlation plots.
    # See https://en.wikipedia.org/wiki/Binding_constant
    ideal_gas_constant = 8.31446261815324  # J/(Mol*K)
    kcal_per_joule = 4184
    # NOTE: Unfortunately, the temperature at which experimental kd
    # binding data was taken
    # is often not recorded. Thus, we are forced to guess. The two standard guesses are
    # physiological body temperature (310K) or room temperature (298K).
    temperature = 298
    rt = (ideal_gas_constant / kcal_per_joule) * temperature
    # NOTE: For performance, simulations are often done in a very small unit cell, and
    # thus at a very high concentration. The size of the unit cell bounds the volume.
    # For shorter simulations where the ligand has not explored the entire box, it may
    # be less. See the Yank paper for a method of calculating the correct volumes.
    standard_concentration = 1  # Units of mol / L, but see comment above.
    return rt * math.log(kd / standard_concentration)


def load_data(  # noqa: PLR0913
    input_excel_path: Path,
    query: str,
    smiles_column: str,
    binding_data_column: str,
    output_txt_path: str,
    min_row: int = 1,
    max_row: int = -1,
    convert_kd_dg: bool = False,
) -> None:
    """Reads SMILES strings and numerical binding affinity data.

    from the given Excel spreadsheet using a Pandas query.

    Args:
        input_excel_path: (Path): Path to the input xlsx file
        query (str): The Query to perform
        min_row (int): min index of rows. Defaults to 1.
        max_row (int): max index of rows. Defaults to -1.
        smiles_column (str): The name of smiles column
        binding_data_column (str): The name of the binding data column
        convert_kd_dg (bool): If this set to True,
        The dG will be calculated. Defaults to False.
        output_txt_path (str): The output text file
    """
    df = pandas.read_excel(str(input_excel_path), sheet_name=1)  # Requires openpyxl
    # 'Focus_Reduction_Assay', 'Proliferation', 'Antigen_Expression', \
    # 'Staining_Based', \
    # 'Flourescence', 'Viral_Titer', 'Cell_Viability_By_Neutral_Red_Uptake', \
    # 'eGFP_Reduction', \
    # 'Viral_Infection', 'Microscopy', 'Immunodetection', 'Replicon_Assay', \
    # 'Antigen_Synthesis', \
    # 'Luciferase_Reporter_Assay', 'Viral_Entry', 'MTT_Assay', 'RT-PCR', 'Cytopathy', \
    # 'Flow_Cytometry', \
    # 'Colorimetric', 'Luciferase_Reporter_Gene', 'Cell_Titer', 'Western_Blot', \
    # 'Cytotoxicity',\
    # 'SDS-PAGE', \
    # 'Fluorescence', 'Image-Based', \
    # 'Crystal_Violet_Staining_Assay', \
    # 'Viral_Reduction_Assay']
    # Standard Type ['IC50', 'EC90', 'Inhibition', 'Kd', 'EC50', 'Activity', 'Ki']
    # Standard Relation [nan, "<'", "<='", ">'", "='", ">='"]
    # Standard Units [nan, 'uM', '%']

    df = df.query(query)

    # Perform row slicing (if any)
    if int(min_row) != 1 or int(max_row) != -1:
        # We want to convert to zero-based indices and we also want
        # the upper index to be inclusive (i.e. <=) so -1 lower index.
        df = df[(int(min_row) - 1) : int(max_row)]

    # Now restrict to the columns we actually care about.
    columns = [smiles_column, binding_data_column]
    df = df[columns].dropna()

    # Generate 2D and/or 3D conformers
    smiles_binding_data: list[str] = []
    for idx, row in enumerate(df.values):
        (smiles, binding_datum) = row
        micromolar = 0.000001  # uM
        binding_datum = binding_datum * micromolar

        if convert_kd_dg:
            dg = calculate_dg(binding_datum)
            smiles_binding_data.append(f"{smiles} {binding_datum} {dg}")
        else:
            smiles_binding_data.append(f"{smiles} {binding_datum}")

        # See https://www.rdkit.org/docs/GettingStartedInPython.html#working-with-3d-molecules
        mol_2d: rdkit.Chem.rdchem.Mol = Chem.MolFromSmiles(
            smiles,
        )  # pylint: disable=c-extension-no-member,no-member
        AllChem.Compute2DCoords(mol_2d)  # pylint: disable=no-member

        # rdkit.Chem.rdmolops.AddHs
        # NOTE: "Much of the code assumes that Hs are not included in
        # the molecular topology,
        # so be very careful with the molecule that comes back from this function."
        mol_3d = Chem.AddHs(mol_2d)  # pylint: disable=no-member
        AllChem.EmbedMolecule(mol_3d)  # pylint: disable=no-member
        AllChem.MMFFOptimizeMolecule(mol_3d)  # pylint: disable=no-member

        filename = f"ligand_{idx}.sdf"  # chemblid is NOT unique!
        writer = Chem.SDWriter(filename)  # pylint: disable=no-member
        writer.write(mol_3d)
        writer.close()

    with Path(output_txt_path).open(mode="w", encoding="utf-8") as f:
        f.write("\n".join(smiles_binding_data))
