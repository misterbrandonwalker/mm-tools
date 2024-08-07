# pylint: disable=E0401,E1101,I1101
"""Filter molecules with kekulization errors.

Handle molecules with sanitization errors by assign formal charge based on
valence.
"""
# https://depth-first.com/articles/2020/02/10/a-comprehensive-treatment-of-aromaticity-in-the-smiles-language/
import logging
from os import environ
from pathlib import Path

import rdkit
import typer
from rdkit import Chem
from rdkit.Chem import AllChem

app = typer.Typer()

# Set up logging parameters
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "WARNING"))
logger = logging.getLogger("polus.mm.utils.sanitize_ligand")
logger.setLevel(POLUS_LOG)


def adjust_formal_charges(molecule: Chem.SDMolSupplier) -> Chem.SDMolSupplier:
    """Correct formal charges based on valence.

    Sometimes input structures do not have correct formal charges
    corresponding to bond order topology. So choose to trust bond orders
    assigned and generate formal charges based on that.
    Explicit valence determined what the formal charge should be from
    dictionary of valence to formal charge for that atomic number.
    Special case if atom == carbon or nitrogen and if neighbors contain
    nitrogen, oyxgen or sulfur (polarizable atoms) then if carbon and
    explicit valence only 3, give formal charge of +1
    (more stable then -1 case).

    Args:
        molecule (Chem.SDMolSupplier): The rdkit molecule object

    Returns:
        Chem.SDMolSupplier: Molecule object with adjusted formal charges
    """
    atomicnumtoformalchg: dict[int, dict[int, int]] = {
        1: {2: 1},
        5: {4: 1},
        6: {3: -1},
        7: {2: -1, 4: 1},
        8: {1: -1, 3: 1},
        15: {4: 1},
        16: {1: -1, 3: 1, 5: -1},
        17: {0: -1, 4: 3},
        9: {0: -1},
        35: {0: -1},
        53: {0: -1},
    }
    for atom in molecule.GetAtoms():
        atomnum = atom.GetAtomicNum()
        val = atom.GetExplicitValence()
        if atomicnumtoformalchg.get(atomnum) is None:
            continue
        valtochg = atomicnumtoformalchg[atomnum]
        chg = valtochg.get(val, 0)
        # special case of polar neighbors surrounding carbon or nitrogen
        # https://docs.eyesopen.com/toolkits/cpp/oechemtk/valence.html#openeye-charge-model
        #
        # See Section 6: Factors That Stabilize Carbocations - Adjacent Lone Pairs
        # https://www.masterorganicchemistry.com/2011/03/11/3-factors-that-stabilize-carbocations/#six
        polneighb = False
        if atomnum in (6, 7):
            for natom in atom.GetNeighbors():
                natomicnum = natom.GetAtomicNum()
                if natomicnum in (7, 8, 16):
                    polneighb = True
            num_neighbs = 3
            carbon_atomic_num = 6
            if polneighb and val == num_neighbs and atomnum == carbon_atomic_num:
                chg = 1

        atom.SetFormalCharge(chg)
    return molecule


def generate_conformer(molecule: Chem.SDMolSupplier) -> None:
    """Generate conformer for molecule.

      Generate conformer for molecule. Sometimes rdkit embedding can fail,
      so use random coordinates if failed at first.

    Args:
        molecule (Chem.SDMolSupplier): _description_
    """
    ps = AllChem.ETKDGv2()
    confid = AllChem.EmbedMolecule(molecule, ps)
    if confid == -1:
        ps.useRandomCoords = True
        AllChem.EmbedMolecule(molecule, ps)
        # only want to catch error Bad Conformation Id,
        # dont need to spend time optimizing
        AllChem.MMFFOptimizeMolecule(molecule, confId=0, maxIters=1)


def is_valid_ligand(molecule: Chem.SDMolSupplier) -> bool:
    """Check if ligand is valid.

    Args:
        molecule (Chem.SDMolSupplier): The rdkit small molecule object

    Returns:
        bool: if ligand is valid
    """
    try:
        Chem.SanitizeMol(molecule)
        return True
    except:  # pylint: disable=broad-exception-caught # noqa: E722
        return False


def attempt_fix_ligand(
    molecule: Chem.SDMolSupplier,
) -> tuple[bool, Chem.SDMolSupplier]:
    """Attempt to fix ligand if not valid.

       Check for sanitization errors, attempt to fix formal
       charges/valence consistency errors. DiffDock uses rdkit
       to generate a seed conformation that will sometimes crash,
       so generating conformations here to catch that error and
       prevent DiffDock from running that ligand.

    Args:
        molecule (Chem.SDMolSupplier): The rdkit small molecule object

    Returns:
        bool: if ligand is valid
        Chem.SDMolSupplier: molecule object
    """
    valid_lig = True
    try:
        Chem.SanitizeMol(molecule)
        generate_conformer(molecule)
    except rdkit.Chem.rdchem.KekulizeException as e:
        valid_lig = False
        logger.warning(f"KekulizeException: {e}")
        # Not handling kekulization error now so just remove file
        # to prevent DiffDock execution
    except rdkit.Chem.rdchem.MolSanitizeException:
        # can also be explicit valence error (i.e.) formal charge
        # not consistent with bond topology
        # choose to trust bond topology around atom and add formal
        # charge based on that
        molecule = adjust_formal_charges(molecule)
    except ValueError as e:
        # assuming this is Bad Conformer Id error
        # from generate_conformer
        valid_lig = False
        logger.warning(f"ValueError: {e}")
    except Exception as e:  # pylint: disable=broad-exception-caught # noqa: BLE001
        # catch *all* exceptions rdkit can throw
        valid_lig = False
        logger.warning(f"Exception: {e}")

    return valid_lig, molecule


def sanitize_the_ligand(input_small_mol_ligand: Path) -> None:
    """Sanitize ligand file.

    Args:
        input_small_mol_ligand: Ligand file
    """
    output_small_mol_ligand = Path(input_small_mol_ligand)
    mol: Chem.SDMolSupplier = Chem.SDMolSupplier(
        input_small_mol_ligand,
        sanitize=False,
        removeHs=False,
    )[0]

    valid_ligand = is_valid_ligand(mol)
    if not valid_ligand:
        valid_ligand, rdkit_mol = attempt_fix_ligand(mol)
    else:
        rdkit_mol = mol

    if valid_ligand:
        with Chem.SDWriter(output_small_mol_ligand) as w:
            w.write(rdkit_mol)

    outdir = Path.cwd()
    with outdir.joinpath("valid.txt").open("w", encoding="utf-8") as f:
        f.write(str(valid_ligand))
