# autodock_vina_run (0.1.0)

Wrapper of the AutoDock Vina software.

## Options

This plugin takes 6 input arguments and 2 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_ligand_pdbqt_path | Path to the input PDBQT ligand, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_ligand.pdbqt | Input | File | File |
| input_receptor_pdbqt_path | Path to the input PDBQT receptor, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_receptor.pdbqt | Input | File | File |
| input_box_path | Path to the PDB containig the residues belonging to the binding site, Type: string, File type: input, Accepted formats: pdb, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/vina/vina_box.pdb | Input | File | File |
| output_pdbqt_path | Path to the output PDBQT file, Type: string, File type: output, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.pdbqt | Input | string | string |
| output_log_path | Path to the log file, Type: string, File type: output, Accepted formats: log, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.log | Input | string | string |
| config | Advanced configuration options for biobb_vs AutoDockVinaRun. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_vs AutoDockVinaRun documentation: https://biobb-vs.readthedocs.io/en/latest/vina.html#module-vina.autodock_vina_run | Input | string | string |
| output_pdbqt_path | Path to the output PDBQT file | Output | File | File |
| output_log_path | Path to the log file | Output | File | File |
