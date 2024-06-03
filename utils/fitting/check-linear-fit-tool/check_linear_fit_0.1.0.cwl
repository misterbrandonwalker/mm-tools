#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: check_linear_fit

doc: |-
  check_linear_fit

baseCommand: ["python", "-m", "polus.mm.utils.check_linear_fit"]

requirements:
  DockerRequirement:
    dockerPull: polusai/check-linear-fit-tool@sha256:20c3056601a244cfde2878cfe04ffc210ee7de6062065cbefe2a8fa0a69d4a0e
  InlineJavascriptRequirement: {}

inputs:

  xs:
    type:
      type: array
      items: float
    inputBinding:
      prefix: --xs

  ys:
    type:
      type: array
      items: float
    inputBinding:
      prefix: --ys

  tol_quad:
    type: float
    inputBinding:
      prefix: --tol_quad

  slope_min:
    type: float
    inputBinding:
      prefix: --slope_min

  slope_max:
    type: float
    inputBinding:
      prefix: --slope_max

outputs:
  success:
    type: boolean
    outputBinding:
      outputEval: $(true)  # If check_linear_fit.py didn't call sys.exit(1), then it called sys.exit(0)

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
