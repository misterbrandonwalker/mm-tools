# onionnet-sfct (0.1.0)

OnionNet-SFCT tool for rescoring of docking poses

## Options

This plugin takes 6 input arguments and 4 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| receptor_path | Receptor file | Input | File | File |
| ligand_path | Ligand file | Input | File | File |
| model_path | model file | Input | string | string |
| pose_type | Type of pose ("vina", "smina", "gnina", "idock", "ledock") | Input | string | string |
| output_score_path | Output score filename | Input | string | string |
| output_path | Output file path | Input | string | string |
| output_score_path | Output score file | Output | File | File |
| output_path | Output file | Output | File | File |
| output_docking_score | Estimated Free Energy of Binding | Output | float | float |
| output_poses_rescore | Estimated Free Energy of Binding | Output | float | float |
