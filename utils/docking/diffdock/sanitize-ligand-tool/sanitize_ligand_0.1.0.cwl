#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Sanitize input ligand

doc: |-
  Sanitize input ligand

baseCommand: ["python", "-m", "polus.mm.utils.sanitize_ligand"]

hints:
  DockerRequirement:
    dockerPull:  polusai/sanitize-ligand-tool@sha256:7a98c3698a560d75efd84251464a0f1b722972c5a20a828f58c211419281cd79

requirements:
  InlineJavascriptRequirement: {}
  InitialWorkDirRequirement: # conditionally overwrite the input ligand, otherwise cwltool will symlink to the original
    listing:
      - $(inputs.input_small_mol_ligand)

inputs:

  input_small_mol_ligand:
    type: File
    format:
      - edam:format_3814
    inputBinding:
      prefix: --input_small_mol_ligand

outputs:

  output_ligand:
    type: File
    format: edam:format_3814
    outputBinding:
      glob: "*.sdf"

  valid_ligand:
    type: boolean
    outputBinding:
      glob: valid.txt
      loadContents: true
      outputEval: |
        ${
          // Read the contents of the file
          const lines = self[0].contents.split("\n");
          // Read boolean value from the first line
          const valid = lines[0].trim() === "True";
          return valid;

        }

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
