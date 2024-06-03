#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Sanitize input ligand

doc: |-
  Sanitize input ligand

baseCommand: ["python", "-m", "polus.mm.utils.sanitize_ligand"]

hints:
  DockerRequirement:
    dockerPull:  polusai/sanitize-ligand-tool@sha256:926e501300fa5b940c250347cf346cdcacf21944469ed82c3788a58e0957c18d

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

  stderr:
    type: File
    outputBinding:
      glob: stderr

  stdout:
    type: File
    outputBinding:
      glob: stdout

stderr: stderr

stdout: stdout

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
