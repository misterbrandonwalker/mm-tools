#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Download MolGAN models and datasets

doc: |
  Download MolGAN models and datasets

baseCommand: ["bash", "/MolGAN/data/download_dataset.sh"]

hints:
  DockerRequirement:
    dockerPull: polusai/molgan-tool@sha256:e008e74170be12dcf50a936a417b8c330ccdebf7fe17abaa8fa2689dac210725

inputs:
  output_sdf_path:
    label: Path to the output file
    doc: |-
      Path to the output file
      Type: string
      File type: output
      Accepted formats: sdf
    type: string
    format: edam:format_3814 # sdf
    default: system.sdf
    inputBinding:
      position: 1

  output_NP_Score_path:
    label: Output ceout file (AMBER ceout)
    doc: |-
      Output ceout file (AMBER ceout)
      Type: string
      File type: output
      Accepted formats: gz
      Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz
    type: string?
    format: edam:format_3987
    default: NP.gz
    inputBinding:
      position: 2

  output_SA_Score_path:
    label: Output ceout file (AMBER ceout)
    doc: |-
      Output ceout file (AMBER ceout)
      Type: string
      File type: output
      Accepted formats: gz
      Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz
    type: string?
    format: edam:format_3987
    default: SA.gz
    inputBinding:
      position: 3


outputs:
  output_sdf_path:
    label: Path to the output file
    doc: |-
      Path to the output file
    type: File
    outputBinding:
      glob: $(inputs.output_sdf_path)
    format: edam:format_3814 # sdf

  output_NP_Score_path:
    label: Output ceout file
    doc: |-
      Output ceout file
    type: File
    outputBinding:
      glob: $(inputs.output_NP_Score_path)
    format: edam:format_3987 # gz

  output_SA_Score_path:
    label: Output ceout file
    doc: |-
      Output ceout file
    type: File
    outputBinding:
      glob: $(inputs.output_SA_Score_path)
    format: edam:format_3987 # gz

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
