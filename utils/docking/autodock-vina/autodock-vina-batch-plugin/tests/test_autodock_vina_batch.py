"""Tests for autodock_vina_batch."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_autodock_vina_batch() -> None:
    """Test autodock_vina_batch."""
    cwl_file_str = "autodock_vina_batch_0@1@0.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)

    # Create a Step instance for the CWL tool
    autodock_step = Step(clt_path=cwl_file)
    autodock_step.input_batch_pdbqt_path = [
        {
            "class": "File",
            "path": str(Path(__file__).resolve().parent / Path("vina_ligand.pdbqt")),
        },
    ]

    autodock_step.input_receptor_pdbqt_path = str(
        Path(__file__).resolve().parent / Path("vina_receptor.pdbqt"),
    )
    autodock_step.input_box_path = str(
        Path(__file__).resolve().parent / Path("vina_box.pdb"),
    )
    autodock_step.output_log_path = "system.log"

    # Create and run the Workflow
    workflow = Workflow([autodock_step], "autodock_vina_batch")
    workflow.run()

    # Verify the output
    outdir = Path("outdir")
    files = list(outdir.rglob("system.log"))

    assert (
        files
    ), f"The file 'system.log' does not exist in any subdirectory of '{outdir}'."
