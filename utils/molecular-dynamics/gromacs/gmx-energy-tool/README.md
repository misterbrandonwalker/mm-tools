# gmx_energy (0.1.0)

Wrapper of the GROMACS energy module for extracting energy components from a given GROMACS energy file.

## Options

This plugin takes 3 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_energy_path | Path to the input EDR file, Type: string, File type: input, Accepted formats: edr, Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/data/gromacs/energy.edr | Input | File | File |
| output_xvg_path | Path to the XVG output file, Type: string, File type: output, Accepted formats: xvg, Example file: https://github.com/bioexcel/biobb_analysis/raw/master/biobb_analysis/test/reference/gromacs/ref_energy.xvg | Input | string | string |
| config | Advanced configuration options for biobb_analysis GMXEnergy. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_analysis GMXEnergy documentation: https://biobb-analysis.readthedocs.io/en/latest/gromacs.html#module-gromacs.gmx_energy | Input | string | string |
| output_xvg_path | Path to the XVG output file | Output | File | File |
