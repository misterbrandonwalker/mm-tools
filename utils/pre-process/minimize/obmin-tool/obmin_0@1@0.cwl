#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Run a Bash script

doc: |
  Run a Bash script

baseCommand: bash

hints:
  DockerRequirement:
    dockerPull: polusai/openbabel-tool@sha256:e685b764da702f37da5688766f976fc4b989054e090830e9c95c2510fe3112c6

inputs:
  script:
    type: string
    inputBinding:
      position: 1

  input_mol2_path:
    type: File
    format: edam:format_3816
    inputBinding:
      position: 2

  output_mol2_path:
    type: string
    format: edam:format_3816
#    inputBinding:
#      position: 3
    default: system.mol2

outputs:
  output_mol2_path:
    type: File
    format: edam:format_3816 # 'Textual format'
    streamable: true
    outputBinding:
      glob: $(inputs.output_mol2_path)

stdout: $(inputs.output_mol2_path)

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
