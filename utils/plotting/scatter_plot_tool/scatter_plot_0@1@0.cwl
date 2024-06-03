#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Generate a scatter plot

doc: |-
  Generate a scatter plot

baseCommand: ["python", "-m", "polus.mm.utils.scatter_plot"]

hints:
  DockerRequirement:
    dockerPull: polusai/scatter-plot-tool@sha256:00a025a1bc943207d8c938af07deb763f6ae1a3a67e94316ea64302427f1de8f

inputs:

  xs:
    type:
      type: array
      items: float
    inputBinding:
      position: 2
      prefix: --xs
    doc: |-
      X-axis array of data

  ys:
    type:
      type: array
      items: float
    inputBinding:
      position: 3
      prefix: --ys
    doc: |-
      Y-axis array of data

  ys2:
    type:
      type: array
      items: float
    inputBinding:
      position: 4
      prefix: --ys2
    doc: |-
      Alternative Y-axis array of data

  output_png_path:
    label: Path to the output png file
    doc: |-
      Path to the output png file
    type: string
    format:
    - edam:format_3603 # png
    inputBinding:
      position: 1
      prefix: --output_png_path
    default: scatter.png

outputs:
  output_png_path:
    label: Path to the output png file
    doc: |-
      Path to the output png file
    type: File
    format: edam:format_3603 # png
    outputBinding:
      glob: $(inputs.output_png_path)

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
