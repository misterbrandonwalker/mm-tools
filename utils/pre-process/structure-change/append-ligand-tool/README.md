# append_ligand (0.1.0)

This class takes a ligand ITP file and inserts it in a topology.

## Options

This plugin takes     5     input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_top_zip_path | Path the input topology TOP and ITP files zipball, Type: string, File type: input, Accepted formats: zip, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/data/gromacs_extra/ndx2resttop.zip | Input | File | File |
| input_itp_path | Path to the ligand ITP file to be inserted in the topology, Type: string, File type: input, Accepted formats: itp, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/data/gromacs_extra/pep_ligand.itp | Input | File | File |
| output_top_zip_path | Path/Name the output topology TOP and ITP files zipball, Type: string, File type: output, Accepted formats: zip, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/reference/gromacs_extra/ref_appendligand.zip | Input | string | string |
| input_posres_itp_path | Path to the position restriction ITP file, Type: string, File type: input, Accepted formats: itp, Example file: null | Input | File | File |
| config | Advanced configuration options for biobb_gromacs AppendLigand. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_gromacs AppendLigand documentation: https://biobb-gromacs.readthedocs.io/en/latest/gromacs_extra.html#gromacs-extra-append-ligand-module | Input | string | string |
| output_top_zip_path | Path/Name the output topology TOP and ITP files zipball | Output | File | File |
