# diffdock (0.1.0)

DiffDock Diffusion based protein ligand docking

## Options

This plugin takes     11     input arguments and 4 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| protein_path | Protein input file | Input | File | File |
| ligand_path | Ligand input file | Input | File | File |
| inference_steps | Number of inference steps for diffusion | Input | int | int |
| samples_per_complex | Number of pose samples to generate per complex | Input | int | int |
| batch_size | Batch size | Input | int | int |
| out_dir | Output directory to save poses | Input | string | string |
| model_dir | Input model directory to use | Input | string | string |
| confidence_model_dir | Input confidence model directory | Input | string | string |
| complex_name | Name of complex | Input | string | string |
| max_confident_pose | Highest confident pose | Output | File | File |
| output_files | The output poses | Output | File[] | File[] |
| execution_time | Time to run DiffDock | Output | float | float |
