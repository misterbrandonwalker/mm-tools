# acpype (0.1.0)

This class is a wrapper of Acpype tool for generation of topologies for GROMACS.

## Options

This plugin takes     8     input arguments and 4 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_path | Path to the input file, Type: string, File type: input, Accepted formats: pdb, mdl, mol2, Example file: https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2 | Input | File | File |
| output_gro_path | Path to the GRO output file, Type: string, File type: output, Accepted formats: gro, Example file: https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.gro | Input | string | string |
| output_itp_path | Path to the ITP output file, Type: string, File type: output, Accepted formats: itp, Example file: https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.itp | Input | string | string |
| output_top_path | Path to the TOP output file, Type: string, File type: output, Accepted formats: top, Example file: https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.top | Input | string | string |
| base_name | Prefix for the output filenames, Type: string | Input | string | string |
| charge_method | Method to determine the atomic partial charges, Type: string | Input | string | string |
| net_charge | net molecular charge (int), for gas default is 0, Type: int | Input | int | int |
| output_pdb_path | Path to the PDB output file, Type: string, File type: output, Accepted formats: pdb, #Example file: | Input | string | string |
| output_gro_path | Path to the GRO output file | Output | File | File |
| output_itp_path | Path to the ITP output file | Output | File | File |
| output_top_path | Path to the TOP output file | Output | File | File |
| output_pdb_path | Path to the TOP output file | Output | File | File |
