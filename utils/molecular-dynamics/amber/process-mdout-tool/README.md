# process_mdout (0.1.0)

Wrapper of the AmberTools (AMBER MD Package) process_mdout tool module.

## Options

This plugin takes 3 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_log_path | AMBER (sander) MD output (log) file, Type: string, File type: input, Accepted formats: log, out, txt, o, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/process/sander.heat.log | Input | File | File |
| output_dat_path | Dat output file containing data from the specified terms along the minimization process, Type: string, File type: output, Accepted formats: dat, txt, csv, Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/reference/process/sander.md.temp.dat | Input | string | string |
| config | Advanced configuration options for biobb_amber.process.process_mdout ProcessMDOut. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_amber.process.process_mdout ProcessMDOut documentation: https://biobb-amber.readthedocs.io/en/latest/process.html#module-process.process_mdout | Input | string | string |
| output_dat_path | Dat output file containing data from the specified terms along the minimization process | Output | File | File |
