# zip_top (0.1.0)

zips a gromacs topology TOP file (and/or itp include file).

## Options

This plugin takes 3 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_top_path | Input topology file, Type: string, File type: input, Accepted formats: top, Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/data/gromacs/mdrun.top | Input | File | File |
| input_itp_path | Input topology include file, Type: string, File type: input, Accepted formats: top, Example file: https://github.com/bioexcel/biobb_md/raw/master/biobb_md/test/data/gromacs/mdrun.top | Input | File | File |
| output_top_zip_path |  | Input | string | string |
| output_top_zip_path | Output zip file, Type: string, File type: output, Format: zip, Example file: https://github.com/bioexcel/biobb_md/blob/master/biobb_md/test/data/gromacs/genion.zip | Output | File | File |
