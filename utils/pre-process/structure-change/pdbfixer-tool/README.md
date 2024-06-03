# pdb_fixer (0.1.0)

A tool that fixes structural issues in proteins

## Options

This plugin takes 9 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_pdb_path | The input PDB path | Input | File | File |
| input_helper_pdb_path | Template input PDB path | Input | File | File |
| pdbid | PDB id from RCSB? | Input | string | string |
| url | URL to retrieve PDB from | Input | string | string |
| output_pdb_path | Output protein file path name | Input | string | string |
| add_atoms | What missing atoms to add, all, heavy or none | Input | string | string |
| add_residues | If set to True, adds missing residue | Input | boolean | boolean |
| replace_nonstandard | Replace nonstandard residues with standard equivalents | Input | boolean | boolean |
| keep_heterogens | What heterogens to keep, all, water or none | Input | string | string |
| output_pdb_path | Output protein file path | Output | File | File |
