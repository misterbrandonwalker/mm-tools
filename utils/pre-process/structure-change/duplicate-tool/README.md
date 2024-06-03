# duplicate (0.1.0)

Duplicates a pdbqt file n times, where n is the length of another array.

## Options

This plugin takes     2     input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_pdbqt_singleton_path | Path to the input PDBQT file to be duplicated, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_ligand.pdbqt | Input | File | File |
| input_pdbqt_array_path | Path to the input PDBQT file array, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_ligand.pdbqt | Input | File[] | File[] |
| output_pdbqt_path | Path to the output PDBQT files | Output | File[] | File[] |
