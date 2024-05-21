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
    cwl_file = Path("pdb_fixer_0@1@0.cwl")

    # Create a Step instance
    pdb_fixer_step = Step(clt_path=cwl_file)

    # Define input paths and parameters
    input_pdb_path = str(Path(__file__).resolve().parent / "1msn_protein.pdb")
    input_helper_pdb_path = str(Path(__file__).resolve().parent / "1msn_protein.pdb")
    output_pdb_path = "output.pdb"

    # Assign inputs to the step
    pdb_fixer_step.input_pdb_path = input_pdb_path
    pdb_fixer_step.input_helper_pdb_path = input_helper_pdb_path
    pdb_fixer_step.output_pdb_path = output_pdb_path

    # Create a Workflow instance
    steps = [pdb_fixer_step]
    viz = Workflow(steps, "pdb_fixer")

    # Run the workflow
    viz.run()

    # Check if the expected output file exists
    outdir = Path("outdir")
    files = list(outdir.rglob(output_pdb_path))

    assert (
        files
    ), f"The file '{output_pdb_path}' does not exist in any subdirectory of '{outdir}'."
