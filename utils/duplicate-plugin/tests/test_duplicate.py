"""Tests for duplicate."""
import subprocess
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML


def parse_cwl_arguments(cwl_file: str) -> dict[str, Any]:
    """Parse the CWL file to get the required inputs.

    Args:
        cwl_file (str): The path to the CWL file.

    Returns:
        Dict[str, Dict]: A dictionary of input names to their properties.
    """
    yaml = YAML(typ="safe", pure=True)
    with Path(cwl_file).open(encoding="utf-8") as file:
        cwl_content = yaml.load(file)
    black_list_cwl_types = ["string?", "boolean?"]
    input_to_props: dict[str, Any] = {}
    inputs = cwl_content.get("inputs", {})
    for input_name, input_data in inputs.items():
        default_value = input_data.get("default", "")
        cwl_type = input_data.get("type", "")
        # find inputs that are required
        if not default_value and cwl_type not in black_list_cwl_types:
            if cwl_type == "File" or cwl_type == "File?":
                cwl_format = input_data.get("format", "")
                file_dict = {"class": cwl_type, "path": "", "format": cwl_format}
                input_to_props[input_name] = file_dict
            elif cwl_type == "File[]":
                input_to_props[input_name] = []
                file_dict = {"class": "File", "path": "", "format": cwl_format}
                input_to_props[input_name].append(file_dict)
            else:
                input_to_props[input_name] = ""

    return input_to_props


def create_input_yaml(input_to_value: dict[str, str], output_yaml: str) -> None:
    """Create the input YAML file.

    Args:
        input_to_value (Dict[str, str]): Dictionary of input names to their values.
        output_yaml (str): Path to the output YAML file.
    """
    yaml = YAML()
    with Path(output_yaml).open("w", encoding="utf-8") as file:
        yaml.dump(input_to_value, file)


def test_duplicate() -> None:
    """Test pdb."""
    cwl_file = "duplicate.cwl"

    input_to_props = parse_cwl_arguments(cwl_file)
    file_path = "1msn_protein.pdb"
    file_path = str(Path(__file__).resolve().parent / Path(file_path))
    input_to_props["input_pdbqt_singleton_path"]["path"] = file_path
    file_dict = input_to_props["input_pdbqt_array_path"][0]
    repeats = 2
    input_to_props["input_pdbqt_array_path"] = []
    for i in range(repeats):  # noqa: B007
        file_dict["path"] = file_path
        input_to_props["input_pdbqt_array_path"].append(file_dict)
    input_yaml_path = "pdb.yml"
    create_input_yaml(input_to_props, input_yaml_path)

    # Generate the cwltool command
    # Just make sure calling cwltool doesnt crash since no outputs
    # This cwl file is just outputting duplicates in an array
    # TODO: cwltool cannot seem to overwrite the same filename?
    command = f"cwltool --debug {cwl_file} {input_yaml_path}"
    subprocess.run(command, shell=True)  # noqa: S602
