# pdbbind_generate_conformers (0.1.0)

Download the PDBbind refined database and generate conformers from SMILES

## Options

This plugin takes 9 input arguments and 3 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| input_excel_path |  | Input | File | File |
| query | query str to search the dataset, Type: string, File type: input, Accepted formats: txt | Input | string | string |
| output_txt_path | Path to the text dataset file, Type: string, File type: output, Accepted formats: txt | Input | string | string |
| output_sdf_path | Path to the input file, Type: string, File type: input, Accepted formats: sdf | Input | string | string |
| min_row | The row min inex, Type: int | Input | int | int |
| max_row | The row max inex, Type: int | Input | int | int |
| smiles_column | The name of the smiles column, Type: string, File type: output, Accepted formats: txt | Input | string | string |
| binding_data_column | The name of the binding data column, Type: string, File type: output, Accepted formats: txt | Input | string | string |
| convert_Kd_dG | If this is set to true, dG will be calculated | Input | boolean | boolean |
| output_txt_path | Path to the txt file | Output | File | File |
| output_sdf_path | Path to the input file, Type: string, File type: input, Accepted formats: sdf | Output | File[] | File[] |
| experimental_dGs | Experimental Free Energies of Binding | Output | float[] | float[] |
