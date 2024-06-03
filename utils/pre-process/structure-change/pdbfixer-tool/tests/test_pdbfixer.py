"""Tests for pdbfixer."""
from pathlib import Path

from polus.mm.utils.pdbfixer.pdbfixer import runpdbfixer
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


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
    cwl_file_str = "pdb_fixer_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent / Path(cwl_file_str)
    # Create a Step instance for pdb_fixer
    pdb_fixer = Step(clt_path=cwl_file)

    # Set input properties
    pdb_fixer.input_pdb_path = str(Path(__file__).resolve().parent / "1msn_protein.pdb")
    pdb_fixer.input_helper_pdb_path = str(
        Path(__file__).resolve().parent / "1msn_protein.pdb",
    )
    pdb_fixer.output_pdb_path = "output.pdb"

    # Define the workflow
    steps = [pdb_fixer]
    filename = "pdb_fixer"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check if the output file exists
    assert Path("output.pdb").exists(), "The file 'output.pdb' does not exist."
