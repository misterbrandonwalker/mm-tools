# sander_mdrun (0.1.0)

Wrapper of the AmberTools (AMBER MD Package) sander tool module.

## Options

This plugin takes 12 input arguments and 6 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_top_path | Input topology file (AMBER ParmTop), Type: string, File type: input, Accepted formats: top, parmtop, prmtop, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/sander/cln025.prmtop | Input | File | File |
| input_crd_path | Input coordinates file (AMBER crd), Type: string, File type: input, Accepted formats: crd, mdcrd, inpcrd, netcdf, nc, ncrst, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/sander/cln025.inpcrd | Input | File | File |
| output_log_path | Output log file, Type: string, File type: output, Accepted formats: log, out, txt, o, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/reference/sander/sander.log | Input | string | string |
| output_traj_path | Output trajectory file, Type: string, File type: output, Accepted formats: trj, crd, mdcrd, x, netcdf, nc, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/reference/sander/sander.x | Input | string | string |
| output_rst_path | Output restart file, Type: string, File type: output, Accepted formats: rst, rst7, netcdf, nc, ncrst, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/reference/sander/sander.rst | Input | string | string |
| input_mdin_path | Input configuration file (MD run options) (AMBER mdin), Type: string, File type: input, Accepted formats: mdin, in, txt, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/sander/npt.mdin | Input | File | File |
| input_cpin_path | Input constant pH file (AMBER cpin), Type: string, File type: input, Accepted formats: cpin, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/sander/cln025.cpin | Input | File | File |
| input_ref_path | Input reference coordinates for position restraints, Type: string, File type: input, Accepted formats: rst, rst7, netcdf, nc, ncrst, crd, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/sander/sander.rst | Input | File | File |
| output_cpout_path | Output constant pH file (AMBER cpout), Type: string, File type: output, Accepted formats: cpout, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/reference/sander/sander.cpout | Input | string | string |
| output_cprst_path | Output constant pH restart file (AMBER rstout), Type: string, File type: output, Accepted formats: cprst, rst, rst7, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/reference/sander/sander.cprst | Input | string | string |
| output_mdinfo_path | Output MD info, Type: string, File type: output, Accepted formats: mdinfo, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/reference/sander/sander.mdinfo | Input | string | string |
| config | Advanced configuration options for biobb_amber SanderMDRun. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_amber SanderMDRun documentation: https://biobb-amber.readthedocs.io/en/latest/sander.html#module-sander.sander_mdrun | Input | string | string |
| output_log_path | Output log file | Output | File | File |
| output_traj_path | Output trajectory file | Output | File | File |
| output_rst_path | Output restart file | Output | File | File |
| output_cpout_path | Output constant pH file (AMBER cpout) | Output | File | File |
| output_cprst_path | Output constant pH restart file (AMBER rstout) | Output | File | File |
| output_mdinfo_path | Output MD info | Output | File | File |
