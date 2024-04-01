# convert_pdbqt (0.1.0)

This class is a wrapper of the Open Babel tool.

## Options

This plugin takes     5     input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| first_molecule | Input Index of the first molecule (1-based), Type: string? | Input | string | string |
| last_molecule | Input Index of the last molecule (1-based), Type: string? | Input | string | string |
| input_path | Path to the input file, Type: string, File type: input, Accepted formats: dat, ent, fa, fasta, gro, inp, log, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt, xml, xtc, Example file: https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.smi | Input | File | File |
| output_pdb_path | Path to the output file, Type: string, File type: output, Accepted formats: pdb | Input | string | string |
| arg1 | Additional arguments, Type: string? | Input | string | string |
| output_pdb_path | Path to the output file | Output | File | File |
