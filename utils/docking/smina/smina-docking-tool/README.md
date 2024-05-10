# smina_docking (0.1.0)

Smina docking tool to perform protein-ligand docking

## Options

This plugin takes 6 input arguments and 2 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| receptor_file | Path to the input receptor file, Type: string?, File type: input, Accepted formats: pdb, pdbqt, sdf, mol, mol2 | Input | File | File |
| ligand_file | Path to the input ligand file, Type: string?, File type: input, Accepted formats: pdb, pdbqt, sdf, mol, mol2 | Input | File | File |
| ligand_box | Path to the input docking box file, Type: string?, File type: input, Accepted formats: pdb, pdbqt, sdf, mol, mol2 | Input | File | File |
| scoring | Which scoring function to use, can be vina, vinardo, or a customized scoring function | Input | string | string |
| output_dock_file | Output dock filename, contains docking poses | Input | string | string |
| output_path | Output file name | Input | string | string |
| output_dock_file | Output dock file, contains docking poses | Output | File | File |
| output_path | Output file | Output | File | File |
