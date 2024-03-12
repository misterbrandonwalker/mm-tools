# pdbbind_refined_v2020 (0.1.0)

Extract pdbbind_refined_v2020 data

## Options

This plugin takes 7 input arguments

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| index_file_name |  | Input | string | string |
| base_dir |  | Input | string | string |
| query | query str to search the dataset. Pandas query doesn't support slash(/) in column names please use Kd_Ki instead of Kd/Ki, Type: string, File type: input, Accepted formats: txt | Input | string | string |
| min_row | The row min inex, Type: int | Input | int | int |
| max_row | The row max inex, Type: int | Input | int | int |
| convert_Kd_dG | If this is set to true, dG will be calculated | Input | boolean | boolean |
