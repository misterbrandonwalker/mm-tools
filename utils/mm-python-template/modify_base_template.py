"""Modify the base template to add input and output options dynamically."""
import contextlib
import json
import shutil
from pathlib import Path

# Load cookiecutter.json
json_path = Path("cookiecutter.json")

with json_path.open() as json_file:
    cookiecutter_data = json.load(json_file)


def add_readme_options_dynamically(cookiecutter_json: dict) -> None:
    """Add the Options section to the README.md file dynamically.

    Args:
        cookiecutter_json (Dict): The cookiecutter.json file as a dictionary.
    """
    # Create the Options section dynamically
    options_section = f"\n## Options\n\nThis plugin takes \
    {len(cookiecutter_json['inputs'])} \
    input arguments and {len(cookiecutter_json['outputs'])} output argument:\n\n"

    # Add the table headers
    options_section += (
        "| Name          | Description             | I/O    | Type   | Default |\n"
    )
    options_section += (
        "|---------------|-------------------------|--------|--------|---------|\n"
    )

    # Add rows for input arguments
    for input_name, input_data in cookiecutter_json["inputs"].items():
        options_section += "| {} | {} | {} | {} | {} |\n".format(
            input_name,
            input_data["description"],
            "Input",
            input_data["type"],
            input_data["type"],
        )

    # Add rows for output arguments
    for output_name, output_data in cookiecutter_json["outputs"].items():
        options_section += "| {} | {} | {} | {} | {} |\n".format(
            output_name,
            output_data["description"],
            "Output",
            output_data["type"],
            output_data["type"],
        )
    path = Path("{{cookiecutter.container_name}}") / "README.md"

    with path.open("a") as updated_readme_file:
        updated_readme_file.write(options_section)

def add_test_content(cookiecutter_json) -> None:
    """Add the test function to the plugin file."""
    package_name = cookiecutter_json["plugin_package"].split(".")[-1]
    def_string = f"def test_{package_name}() -> None:\n"
    def_string += f'    """Test {package_name}."""\n'
    def_string += f"    pass\n"

    path = (
        Path("{{cookiecutter.container_name}}")
        / "tests"
        / "test_{{cookiecutter.package_name}}.py"
    )

    with path.open("a") as file:
        file.write("\n")
        file.write(def_string)


def add_function_arguments_dynamically(cookiecutter_json: dict) -> None:
    """Add the function arguments to the plugin file.

    Args:
        cookiecutter_json (Dict): The cookiecutter.json file as a dictionary.
    """
    package_name = cookiecutter_json["plugin_package"].split(".")[-1]
    def_string = f"def {package_name}("
    dict_items = ["inputs"]

    # create definition string
    for item in dict_items:
        for key, value in cookiecutter_json[item].items():
            if key == "inpdir":
                continue
            if "python_type" in value:
                def_string += f"{key} : {value['python_type']}, "
    def_string = def_string[:-2] + ")"
    # now add the docstring
    docstring = f"    '''{cookiecutter_json['plugin_name']}.\n\n    Args:\n"
    for item in dict_items:
        for key, value in cookiecutter_json[item].items():
            if key == "inpdir":
                continue
            if "python_type" in value:
                docstring += f"        {key}: {value['description']}\n"
    path = (
        Path("{{cookiecutter.container_name}}")
        / "src"
        / "{{cookiecutter.package_folders}}"
        / "{{cookiecutter.package_name}}.py"
    )

    with path.open("a") as file:
        file.write(
            def_string
            + "\n"
            + docstring
            + "    Returns:\n        None\n    '''\n    pass\n",
        )


def add_main_function_dynamically(cookiecutter_json: dict) -> None:
    """Add the main function to the __main__.py file.

    Args:
        cookiecutter_json (Dict): The cookiecutter.json file as a dictionary.
    """
    # Create the main function string
    main_function_string = "\n\n@app.command()\ndef main("

    dict_items = ["inputs"]
    for item in dict_items:
        for key, value in cookiecutter_json[item].items():
            main_function_string += (
                f"\n    {key}: {value['python_type']} = typer.Option("
            )
            main_function_string += "\n        ...,"
            main_function_string += f"\n        '--{key}',"
            main_function_string += f"\n        help='{value['description']}',"
            main_function_string += "\n    ),"

    # Add the main function body
    main_function_string += "\n) -> None:"
    main_function_string += f'\n    """{cookiecutter_json["plugin_name"]}."""'
    for item in dict_items:
        for key in cookiecutter_json[item]:
            main_function_string += f'\n    logger.info(f"{key}: {{{key}}}")'

    package_name = cookiecutter_json["plugin_package"].split(".")[-1]
    main_function_string += f"\n\n    {package_name}("
    for item in dict_items:
        for key in cookiecutter_json[item]:
            main_function_string += f"\n    {key}={key},"
    main_function_string = main_function_string[:-1] + ")"
    main_function_string += "\n\nif __name__ == '__main__':"
    main_function_string += "\n    app()"

    # Check if the __main__.py file exists
    main_file_path = (
        Path("{{cookiecutter.container_name}}")
        / "src"
        / "{{cookiecutter.package_folders}}"
        / "__main__.py"
    )

    with main_file_path.open("a") as file:
        file.write(main_function_string)


def add_ict_inputs_outputs_dynamically(cookiecutter_json: dict) -> None:
    """Add the input and output options to the ict.yml file.

    Args:
        cookiecutter_json (Dict): The cookiecutter.json file as a dictionary.
    """
    path = Path("{{cookiecutter.container_name}}") / "ict.yml"

    array = ["inputs", "outputs"]
    with path.open("a") as updated_ict_file:
        for item in array:
            if len(cookiecutter_json[item]) == 0:
                continue
            updated_ict_file.write(f"{item}:\n")
            for key, value in cookiecutter_json[item].items():
                updated_ict_file.write(f"  - name: {key}\n")
                updated_ict_file.write("    required: true\n")
                # remove character : from description because of yaml
                value["description"] = value["description"].replace(":", "")
                updated_ict_file.write(f"    description: {value['description']}\n")
                updated_ict_file.write(f"    type: {value['type']}\n")
                if "default" in value:
                    updated_ict_file.write(f"    defaultValue: {value['default']}\n")
                if "format" in value:
                    uris = value["format"]
                    if isinstance(uris, list):
                        uris = ", ".join(uris)
                    updated_ict_file.write("    format:\n")
                    updated_ict_file.write(f"      uri: {uris}\n")
        updated_ict_file.write("ui:\n")
        for key, value in cookiecutter_json["inputs"].items():
            updated_ict_file.write(f"  - key: inputs.{key}\n")
            updated_ict_file.write(f'    title: "{key}: "\n')
            updated_ict_file.write(f"    description: \"{value['description']}\"\n")
            # type can be text, number, checkbox, path or file
            # if incoming type is boolean, then type is checkbox
            if value["type"] == "boolean":
                value["type"] = "checkbox"
            updated_ict_file.write(f"    type: {value['type']}\n")


def generate_pydantic_models(cookiecutter_json: dict) -> str:
    """Generate Pydantic models based on cookiecutter data."""

    models_code = ""

    if len(cookiecutter_json["inputs"]) == 1 and list(cookiecutter_json["inputs"].values())[0]['python_type'] == 'Path':
        pass
    else:
        # Input Model (if there are other inputs)
        models_code += "class InputModel(BaseModel):\n"
        for input_name, input_data in cookiecutter_json["inputs"].items():
            # Check if the python_type is Path, and change it to UploadFile for file inputs
            if input_data['python_type'] == 'Path':
                python_type = 'UploadFile'  # For file uploads, use UploadFile
                models_code += f"    {input_name}: {python_type} = File(..., description=\"{input_data['description']}\")\n"
            else:
                python_type = input_data['python_type']  # Use the provided type for other fields
                models_code += f"    {input_name}: {python_type} = Field(..., description=\"{input_data['description']}\")\n"
        models_code += "\n"

    # Output Model
    models_code += "class OutputModel(BaseModel):\n"
    for output_name, output_data in cookiecutter_json["outputs"].items():
        # If it's a file path (Path), use Path directly
        if output_data['python_type'] == 'Path':
            python_type = 'Path'  # Outputs are file paths, so we use Path
            models_code += f"    {output_name}: {python_type} = Field(..., description=\"{output_data['description']}\")\n"
        else:
            python_type = output_data['python_type']  # Use the specified type for other output fields
            models_code += f"    {output_name}: {python_type} = Field(..., description=\"{output_data['description']}\")\n"
    models_code += "\n"

    return models_code


def generate_post_function(cookiecutter_json: dict) -> str:
    """Generate the POST function using FastAPI, dynamically calling the specified function."""
    
    # Extract function name from cookiecutter JSON data
    function_name = cookiecutter_json["plugin_package"].split(".")[-1]
    
    # Start building the function signature for the POST request
    post_code = f"@app.post(\"/process\", response_model=OutputModel)\n"
    post_code += f"async def process_data("
    
    # Add arguments dynamically based on input data
    input_fields = cookiecutter_json["inputs"]
    
    # Loop through the inputs to determine whether they are files or other types
    for input_name, input_data in input_fields.items():
        if input_data['python_type'] == 'Path':
            # If the input type is Path, use UploadFile in the function signature
            post_code += f"{input_name}: UploadFile = File(..., description=\"{input_data['description']}\")\n    "
        else:
            # For other types, use Field to define them
            post_code += f"{input_name}: {input_data['python_type']} = Field(..., description=\"{input_data['description']}\")\n    "
    
    post_code = post_code.strip()  # Remove the extra last newline
    
    # Closing the function definition
    post_code += f"""):\n    \"\"\"Process the input data and return the results.\"\"\"\n\n"""
    
    # Add logic to handle file processing
    post_code += """
    # Handle the uploaded files (save them to disk)
    input_data_dict = {}
"""
    for input_name, input_data in input_fields.items():
        if input_data['python_type'] == 'Path':
            # Handle saving the uploaded file to disk
            post_code += f"""
    if {input_name}:
        file_content = await {input_name}.read()
        file_path = Path.cwd() / {input_name}.filename 
        with open(file_path, 'wb') as f:
            f.write(file_content)
        input_data_dict["{input_name}"] = file_path
"""
    
    # Add the plugin function call, unpacking the input data
    post_code += f"""
    # Dynamically call the plugin function with unpacked input data
    result = {function_name}(**input_data_dict)
    
    # Get the file extension of the input file
    input_file_extension = {input_name}.filename.split('.')[-1]
    
    # Use glob to find files with the same extension as the input file
    output_files = list(Path.cwd().rglob(f"*.{{input_file_extension}}"))
    
    # Use the first file found with the matching extension
    output_file_path = output_files[0]
    
    return FileResponse(output_file_path)
    """
    
    return post_code


def update_server_template(cookiecutter_json: dict) -> None:
    """Update the server template with dynamically generated Pydantic models and POST function."""
    # Path to the template server.py file
    server_template_path = Path("{{cookiecutter.container_name}}") / "src" / "{{cookiecutter.package_folders}}" / "server.py"
    
    # Generate the models and post function code
    models_code = generate_pydantic_models(cookiecutter_json)
    post_code = generate_post_function(cookiecutter_json)
    
    # Uvicorn startup code
    uvicorn_code = """
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
"""

    # Open the server template and append the generated code
    with server_template_path.open("a") as server_file:
        server_file.write("\n\n# Generated Pydantic models\n")
        server_file.write(models_code)
        server_file.write("\n# Generated POST function\n")
        server_file.write(post_code)
        server_file.write("\n# Uvicorn startup code\n")
        server_file.write(uvicorn_code)


# need to handle cases where base_command is just python3
# calling some script already in container for example
ADD_SOURCE = False
base_command = cookiecutter_data["base_command"]
if "arguments" in cookiecutter_data:
    arguments = cookiecutter_data["arguments"]
    # combine base_command and arguments need to determine if source is needed
    base_command = base_command + " " + arguments
# look for .py file in base_command
for item in base_command.split():
    if ".py" in item or "python" in item:
        ADD_SOURCE = True
        break

add_readme_options_dynamically(cookiecutter_data)
add_ict_inputs_outputs_dynamically(cookiecutter_data)
add_test_content(cookiecutter_data)
if ADD_SOURCE:
    add_function_arguments_dynamically(cookiecutter_data)
    add_main_function_dynamically(cookiecutter_data)
    update_server_template(cookiecutter_data)
    cookiecutter_data[
        "base_command"
    ] = f"python3 -m {cookiecutter_data['plugin_package']}"
    with json_path.open("w") as json_file:
        json.dump(cookiecutter_data, json_file, indent=4)
else:
    src_folder = Path("{{cookiecutter.container_name}}") / "src"
    with contextlib.suppress(FileNotFoundError):
        shutil.rmtree(src_folder)

    dockerfile = Path("{{cookiecutter.container_name}}") / "Dockerfile"
    build_docker = Path("{{cookiecutter.container_name}}") / "build-docker.sh"
    dockerfile.unlink()
    build_docker.unlink()

    pyproject = Path("{{cookiecutter.container_name}}") / "pyproject.toml"
    with pyproject.open("r") as read_file:
        lines = read_file.readlines()

    with pyproject.open("w") as write_file:
        for line in lines:
            if "packages = [" not in line:
                write_file.write(line)
