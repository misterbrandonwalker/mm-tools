# mdrun (0.1.0)

Wrapper of the GROMACS mdrun module.

## Options

This plugin takes 10 input arguments and 7 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_tpr_path | Path to the portable binary run input file TPR, Type: string, File type: input, Accepted formats: tpr, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/data/gromacs/mdrun.tpr | Input | File | File |
| output_crd_path | Path to the output GROMACS structure GRO file, Type: string, File type: output, Accepted formats: gro, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/reference/gromacs/ref_mdrun.gro | Input | string | string |
| output_edr_path | Path to the output GROMACS portable energy file EDR, Type: string, File type: output, Accepted formats: edr, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/reference/gromacs/ref_mdrun.edr | Input | string | string |
| output_log_path | Path to the output GROMACS trajectory log file LOG, Type: string, File type: output, Accepted formats: log, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/reference/gromacs/ref_mdrun.log | Input | string | string |
| output_trr_path | Path to the GROMACS uncompressed raw trajectory file TRR, Type: string, File type: output, Accepted formats: trr, Example file: https://github.com/bioexcel/biobb_gromacs/raw/master/biobb_gromacs/test/reference/gromacs/ref_mdrun.trr | Input | string | string |
| input_cpt_path | Path to the input GROMACS checkpoint file CPT, Type: string, File type: input, Accepted formats: cpt, Example file: null | Input | File | File |
| output_xtc_path | Path to the GROMACS compressed trajectory file XTC, Type: string, File type: output, Accepted formats: xtc, Example file: null | Input | string | string |
| output_cpt_path | Path to the output GROMACS checkpoint file CPT, Type: string, File type: output, Accepted formats: cpt, Example file: null | Input | string | string |
| output_dhdl_path | Path to the output dhdl.xvg file only used when free energy calculation is turned on, Type: string, File type: output, Accepted formats: xvg, Example file: null | Input | string | string |
| config | Advanced configuration options for biobb_gromacs Mdrun. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_gromacs Mdrun documentation: https://biobb-gromacs.readthedocs.io/en/latest/gromacs.html#module-gromacs.mdrun | Input | string | string |
| output_crd_path | Path to the output GROMACS structure GRO file | Output | File | File |
| output_edr_path | Path to the output GROMACS portable energy file EDR | Output | File | File |
| output_log_path | Path to the output GROMACS trajectory log file LOG | Output | File | File |
| output_trr_path | Path to the GROMACS uncompressed raw trajectory file TRR | Output | File | File |
| output_xtc_path | Path to the GROMACS compressed trajectory file XTC | Output | File | File |
| output_cpt_path | Path to the output GROMACS checkpoint file CPT | Output | File | File |
| output_dhdl_path | Path to the output dhdl.xvg file only used when free energy calculation is turned on | Output | File | File |
