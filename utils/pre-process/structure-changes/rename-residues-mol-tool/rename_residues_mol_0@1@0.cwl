#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Run a python3 script

doc: |-
  Run a python3 script

baseCommand: ["python", "-m", "polus.mm.utils.rename_residues_mol"]

hints:
  DockerRequirement:
<<<<<<<< HEAD:utils/pre-process/structure-change/rename-residues-mol-tool/rename_residues_mol_0@1@0.cwl
    dockerPull: polusai/rename-residues-mol-tool@sha256:7a2662858f2608b3e1cff6170c65dd9f5c635d2cb5e2735b3f075015a7847f58
========
    dockerPull: polusai/rename-residues-mol-tool@sha256:6ef6a91b88870bd55e1408efd49828d7be35bdb3656847a943232a52d3cd092a
>>>>>>>> fb47176 (rename, use docker hash):utils/pre-process/structure-changes/rename-residues-mol-tool/rename_residues_mol_0@1@0.cwl

inputs:

  input_mol2_path:
    type: File
    format: edam:format_3816 # mol2
    inputBinding:
      position: 1
      prefix: --input_mol2_path

  output_mol2_path:
    label: Path to the output file
    doc: |-
      Path to the output file
    type: string
    format: edam:format_3816 # mol2
    inputBinding:
      position: 2
      prefix: --output_mol2_path
    default: system.mol2

outputs:
  output_mol2_path:
    label: Path to the output file
    doc: |-
      Path to the output file
    type: File
    format: edam:format_3816 # mol2
    outputBinding:
      glob: $(inputs.output_mol2_path)

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
