# autodock_vina_batch (0.1.0)

Wrapper of the AutoDock Vina software.

## Options

This plugin takes 5 input arguments and 2 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_batch_pdbqt_path | Path to the input PDBQT ligands, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_ligand.pdbqt | Input | File[] | File[] |
| input_receptor_pdbqt_path | Path to the input PDBQT receptor, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_receptor.pdbqt | Input | File | File |
| input_box_path | Path to the PDB containing the residues belonging to the binding site, Type: string, File type: input, Accepted formats: pdb, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_box.pdb | Input | File | File |
| output_batch_pdbqt_path | Path to the output PDBQT batch directory, Type: string, File type: output, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.pdbqt | Input | string | string |
| output_log_path | Path to the log file, Type: string, File type: output, Accepted formats: log, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.log | Input | string | string |
| output_batch_pdbqt_path | Path to the output PDBQT files | Output | {'type': 'array', 'items': 'File'} | {'type': 'array', 'items': 'File'} |
| output_log_path | Path to the log file | Output | File | File |
