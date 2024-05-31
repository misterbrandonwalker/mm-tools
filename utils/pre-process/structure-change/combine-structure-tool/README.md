# combine_structure (0.1.0)

A tool that employs RDKit to combine two XYZ structures in a single PDB file.

## Options

This plugin takes     3     input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_structure1 | Input structure 1 file path, Type: string, File type: input, Accepted formats: xyz | Input | File | File |
| input_structure2 | Input structure 2 file path, Type: string, File type: input, Accepted formats: xyz | Input | File | File |
| output_structure_path | Output combined PDB file path, Type: string, File type: output, Accepted formats: pdb, Example file: https://github.com/bioexcel/biobb_structure_utils/raw/master/biobb_structure_utils/test/reference/utils/ref_cat_pdb.pdb | Input | string | string |
| output_structure_path | Output protein file path | Output | File | File |
