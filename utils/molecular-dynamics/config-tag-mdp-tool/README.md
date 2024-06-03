# config_tag_mdp (0.1.0)

Returns a dictionary of the given arguments as a JSON-encoded string.

## Options

This plugin takes 5 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| config | A dictionary of the given arguments as a JSON-encoded string. | Input | string | string |
| nsteps | The number of timesteps | Input | int | int |
| dt | The length of each timestep | Input | float | float |
| ref-t | The nominal temperature | Input | float | float |
| ref-p | The nominal pressure | Input | float | float |
| output_config_string | A dictionary of the given arguments as a JSON-encoded string. | Output | string | string |
