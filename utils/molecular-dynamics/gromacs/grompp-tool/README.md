# grompp (0.1.0)

Wrapper of the GROMACS grompp module.

## Options

This plugin takes 7 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_crd_path | Path to the input GROMACS structure GRO file, Type: string, File type: input, Accepted formats: gro, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/data/gromacs/grompp.gro | Input | File | File |
| input_top_zip_path | Path to the input GROMACS topology TOP and ITP files in zip format, Type: string, File type: input, Accepted formats: zip, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/data/gromacs/grompp.zip | Input | File | File |
| output_tpr_path | Path to the output portable binary run file TPR, Type: string, File type: output, Accepted formats: tpr, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/reference/gromacs/ref_grompp.tpr | Input | string | string |
| input_cpt_path | Path to the input GROMACS checkpoint file CPT, Type: string, File type: input, Accepted formats: cpt, Example file: null | Input | File | File |
| input_ndx_path | Path to the input GROMACS index files NDX, Type: string, File type: input, Accepted formats: ndx, Example file: null | Input | File | File |
| input_mdp_path | Path to the input GROMACS MDP file, Type: string, File type: input, Accepted formats: mdp, Example file: null | Input | File | File |
| config | Advanced configuration options for biobb_gromacs Grompp. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_gromacs Grompp documentation: https://biobb-gromacs.readthedocs.io/en/latest/gromacs.html#module-gromacs.grompp | Input | string | string |
| output_tpr_path | Path to the output portable binary run file TPR | Output | File | File |
