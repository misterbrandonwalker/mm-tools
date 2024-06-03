# extract_model_pdbqt (0.1.0)

Extracts a model from a PDBQT file with several models.

## Options

This plugin takes 3 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_pdbqt_path | Input PDBQT file, Type: string, File type: input, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/data/utils/models.pdbqt | Input | File | File |
| output_pdbqt_path | Output PDBQT file, Type: string, File type: output, Accepted formats: pdbqt, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/utils/ref_extract_model.pdbqt | Input | string | string |
| config | Advanced configuration options for biobb_vs ExtractModelPDBQT. This should be passed as a string containing a dict. The possible options to include here are listed under 'properties' in the biobb_vs ExtractModelPDBQT documentation: https://biobb-vs.readthedocs.io/en/latest/utils.html#module-utils.extract_model_pdbqt | Input | string | string |
| output_pdbqt_path | Output PDBQT file | Output | File | File |
