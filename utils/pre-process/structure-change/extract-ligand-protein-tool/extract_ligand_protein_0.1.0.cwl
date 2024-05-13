#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: A tool that employs OpenMM to extract ligands and protein from a PDB file

doc: |-
  A tool that employs OpenMM to extract ligands and protein from a PDB file

baseCommand: ["python", "-m", "polus.mm.utils.extract_ligand_protein"]

hints:
  DockerRequirement:
    dockerPull: polusai/extract-ligand-protein-tool@sha256:38416f3d020c26869028c6ba66a243882d0b3c5885c79ff68355912ec5768fc1

inputs:
  input_pdb_path:
    label: Input pdb file path
    doc: |-
      Input pdb file path
      Type: string
      File type: input
      Accepted formats: pdb
      Example file: https://github.com/bioexcel/biobb_structure_utils/raw/master/biobb_structure_utils/test/data/utils/cat_protein.pdb
    type: File
    format:
    - edam:format_1476
    inputBinding:
      prefix: --input_pdb_path

  output_pdb_path:
    label: Output pdb file path
    doc: |-
      Output pdb file path
      Type: string
      File type: output
      Accepted formats: pdb
      Example file: https://github.com/bioexcel/biobb_structure_utils/raw/master/biobb_structure_utils/test/reference/utils/ref_cat_pdb.pdb
    type: string
    format:
    - edam:format_1476
    inputBinding:
      prefix: --output_pdb_path
    default: system.pdb

  output_pdb_ligand_path:
    label: Output pdb ligand file path
    doc: |-
      Output pdb ligand file path
      Type: string
      File type: output
      Accepted formats: sdf
    type: string
    format:
    - edam:format_1476
    inputBinding:
      prefix: --output_pdb_ligand_path
    default: ligand_system.pdb

outputs:
  output_pdb_path:
    label: Output pdb file path
    doc: |-
      Output pdb file path
    type: File
    outputBinding:
      glob: $(inputs.output_pdb_path)
    format: edam:format_1476

  output_pdb_ligand_path:
    label: Output ligand pdb file path
    doc: |-
      Output ligand pdb file path
      Use optional File? since ligand may not exist in complex
    type: File?
    outputBinding:
      glob: $(inputs.output_pdb_ligand_path)
    format: edam:format_1476

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
