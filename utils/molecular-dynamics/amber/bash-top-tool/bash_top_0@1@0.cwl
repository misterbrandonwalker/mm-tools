#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Concatentate import statements in AMBER topology file

doc: |
  Concatentate import statements in AMBER topology file

baseCommand: bash

hints:
  DockerRequirement:
    dockerPull: polusai/bash-top-tool@sha256:881d3634bd000a931b3339e8328ee9701190e6ac7b1227082bd095e317d2e551

inputs:
  script:
    type: string
    inputBinding:
      position: 1

  input_top_path:
    type: File
    format: edam:format_3880
    inputBinding:
      position: 2

  output_top_path:
    type: string?
    format: edam:format_2330 # 'Textual format'
#    inputBinding:
#      position: 3
    default: system.top

outputs:
  output_top_path:
    type: File
    format: edam:format_3880
    streamable: true
    outputBinding:
      glob: $(inputs.output_top_path)

stdout: $(inputs.output_top_path)

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
