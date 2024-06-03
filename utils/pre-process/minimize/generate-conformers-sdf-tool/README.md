# generate_conformers_sdf (0.1.0)

Uses openbabel to add hydrogens and minimize a small molecule, search for the lowest energy conformer, then minimize again.

## Options

This plugin takes 2 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_path | Path to the input file, Type: string, File type: input, Accepted formats: dat, ent, fa, fasta, gro, inp, log, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt, xml, xtc, Example file: https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.smi | Input | File | File |
| output_sdf_path | Output SDF input filename | Input | string | string |
| output_sdf_path | Output SDF file | Output | File | File |
