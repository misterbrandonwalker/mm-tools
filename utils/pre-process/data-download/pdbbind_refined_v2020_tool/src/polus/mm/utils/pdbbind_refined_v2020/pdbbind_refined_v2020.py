"""extract pdbbind_refined_v2020."""
import math
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any

import pandas as pd


def pdbbind_refined_v2020(  # noqa: PLR0913
    output_txt_path: str,
    index_file_name: str,
    base_dir: str,
    query: str,
    min_row: int,
    max_row: int,
    convert_kd_dg: bool,
) -> None:
    """pdbbind_refined_v2020.

    Args:
        output_txt_path: Path to the text dataset file
        index_file_name: The PDBbind index file name
        base_dir: The base directory of the dataset
        query: query str to search the dataset.
        min_row: The row min index
        max_row: The row max index
        convert_kd_dg: If this is set to true, dG will be calculated
    Returns:
        None
    """
    load_data(
        index_file_name,
        base_dir,
        query,
        output_txt_path,
        min_row,
        max_row,
        convert_kd_dg,
    )


def calculate_dg(kd: float) -> float:
    """Calculates binding free energy from Kd.

    Args:
        kd (float): The binding affinity of the protein-ligand complex

    Returns:
        float: The binding free energy
    """
    # Calculate the binding free energy from kd so we can make the correlation plots.
    # See https://en.wikipedia.org/wiki/Binding_constant
    ideal_gas_constant = 8.31446261815324  # J/(Mol*K)
    kcal_per_joule = 4184
    # NOTE: Unfortunately, the temperature at which
    # experimental kd binding data was taken
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


def read_index_file(index_file_path: str) -> pd.DataFrame:
    """Reads the PDBbind index file and extracts binding data.

    Args:
        index_file_path (str): The path to the index file

    Returns:
        pd.DataFrame: The kd data
    """
    data: dict[str, Any] = defaultdict(list)
    # The file format
    # PDB code, resolution, release year, -logkd/Ki, kd/Ki, reference, ligand name
    unit_conv = {"uM": 1, "mM": 1000.0, "nM": 0.001, "pM": 0.000001}

    with Path(index_file_path).open(encoding="utf-8") as rfile:
        lines = [line for line in rfile.readlines() if line[0] != "#" and "Kd=" in line]
        for line in lines:
            words = line.split()
            data["PDB_code"].append(words[0])
            data["resolution"].append(words[1])
            data["release_year"].append(words[2])

            # Kd conversion to micro molar
            unit = re.split(r"=[-+]?(?:\d*\.\d+|\d+)", words[4])[1]
            standard_type = re.split(r"=[-+]?(?:\d*\.\d+|\d+)", words[4])[0]
            kd = float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", words[4])[0])
            data["Kd_Ki"].append(standard_type)
            data["value"].append(kd * unit_conv[unit])
            data["ligand_name"].append(re.findall(r"\((.*?)\)", words[7])[0])

    return pd.DataFrame.from_dict(data)


# pylint: disable=too-many-arguments,too-many-locals


def load_data(  # noqa: PLR0913
    index_file_name: str,
    base_dir: str,
    query: str,
    output_txt_path: str,
    min_row: int = 1,
    max_row: int = -1,
    convert_kd_dg: bool = False,
) -> None:
    """Filters Kd data beased on a query.

    Args:
        index_file_name (str): The PDBbind index file name
        base_dir (str): The base directory of the dataset
        query (str): The Query to perform
        output_txt_path (str): The output text file
        min_row (int, optional): min index of rows. Defaults to 1.
        max_row (int, optional): max index of rows. Defaults to -1.
        convert_kd_dg (bool, optional): If this set to True,
        The dG will be calculated. Defaults to False.
    """
    index_file_path = Path(base_dir).joinpath("index", index_file_name)
    df = read_index_file(str(index_file_path))
    # perform query
    df = df.query(query)

    # Perform row slicing (if any)
    if int(min_row) != 1 or int(max_row) != -1:
        # We want to convert to zero-based indices and we also want
        # the upper index to be inclusive (i.e. <=) so -1 lower index.
        df = df[
            (int(min_row) - 1) : int(max_row)
        ]  # pylint: disable=unsubscriptable-object

    # Calculate dG
    df = df[["PDB_code", "value", "Kd_Ki"]]
    binding_data: list[str] = []
    micromolar = 0.000001  # uM
    for _, row in enumerate(df.values):
        (pdbcode, binding_datum, kd_ki) = row
        binding_datum = binding_datum * micromolar

        if convert_kd_dg:
            dg = calculate_dg(binding_datum)
            binding_data.append(f"{pdbcode} {binding_datum} {dg} {kd_ki}")
        else:
            binding_data.append(f"{pdbcode} {binding_datum} {kd_ki}")

    with Path(output_txt_path).open(mode="w", encoding="utf-8") as f:
        f.write("\n".join(binding_data))

    # copy pdb and sdf files
    for _, row in df.iterrows():
        pdbcode = row["PDB_code"]
        source_pdb_path = Path(base_dir).joinpath(pdbcode, f"{pdbcode}_protein.pdb")
        dist_pdb_path = f"{pdbcode}_protein.pdb"
        subprocess.run(
            ["cp", f"{source_pdb_path}", f"{dist_pdb_path}"],  # noqa: S603, S607
            check=True,
        )
        source_sdf_path = Path(base_dir).joinpath(pdbcode, f"{pdbcode}_ligand.sdf")

        dist_sdf_path = f"{pdbcode}_ligand.sdf"
        subprocess.run(
            ["cp", f"{source_sdf_path}", f"{dist_sdf_path}"],  # noqa: S603, S607
            check=True,
        )
