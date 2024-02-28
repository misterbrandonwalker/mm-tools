# extract_ligand_protein (0.1.0)

A tool that employs OpenMM to extract ligands and protein from a PDB file
## Options

This plugin takes 3 input arguments    and 0 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_pdb_path | Input pdb file path, Type: string, File type: input, Accepted formats: pdb, Example file: https://github.com/bioexcel/biobb_structure_utils/raw/master/biobb_structure_utils/test/data/utils/cat_protein.pdb | Input | File | File |
| output_pdb_path | Output pdb file path, Type: string, File type: output, Accepted formats: pdb, Example file: https://github.com/bioexcel/biobb_structure_utils/raw/master/biobb_structure_utils/test/reference/utils/ref_cat_pdb.pdb | Input | string | string |
| output_pdb_ligand_path | Output pdb ligand file path, Type: string, File type: output, Accepted formats: sdf | Input | string | string |
