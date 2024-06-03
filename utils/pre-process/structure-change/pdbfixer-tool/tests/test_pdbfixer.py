"""Tests for pdbfixer."""
import sys
from pathlib import Path

from polus.mm.utils.pdbfixer.pdbfixer import runpdbfixer

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_pdbfixer() -> None:
    """Test pdbfixer."""
    add_atoms = "all"
    add_residues = True
    pdbid = ""
    url = ""
    replace_nonstandard = True
    keep_heterogens = "all"
    input_pdb_path = "1msn_protein.pdb"
    input_helper_pdb_path = "1msn_protein.pdb"
    input_pdb_path = str(Path(__file__).resolve().parent / Path(input_pdb_path))
    input_helper_pdb_path = str(
        Path(__file__).resolve().parent / Path(input_helper_pdb_path),
    )
    output_pdb_path = "test.pdb"
    output_pdb_path = str(Path(__file__).resolve().parent / Path(output_pdb_path))

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

    assert Path(output_pdb_path).exists()


def test_cwl_pdb_fixer() -> None:
    """Test the pdbfixer function in cwltool."""
    cwl_file = Path("pdb_fixer_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    input_pdb_path = "1msn_protein.pdb"
    input_pdb_path = str(Path(__file__).resolve().parent / Path(input_pdb_path))
    input_to_props["input_pdb_path"]["path"] = input_pdb_path
    input_to_props["input_pdb_path"]["class"] = "File"
    input_helper_pdb_path = "1msn_protein.pdb"
    input_helper_pdb_path = str(
        Path(__file__).resolve().parent / Path(input_helper_pdb_path),
    )
    input_to_props["input_helper_pdb_path"]["path"] = input_helper_pdb_path
    input_to_props["input_helper_pdb_path"]["class"] = "File"
    input_to_props["output_pdb_path"] = "output.pdb"
    input_yaml_path = Path("pdb_fixer_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)

    assert Path("output.pdb").exists()
