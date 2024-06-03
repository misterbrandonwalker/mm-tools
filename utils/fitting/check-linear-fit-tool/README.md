# check_linear_fit (0.1.0)

check_linear_fit

## Options

This plugin takes 5 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| xs | x-axis input array | Input | {'type': 'array', 'items': 'float'} | {'type': 'array', 'items': 'float'} |
| ys | y-axis input array | Input | {'type': 'array', 'items': 'float'} | {'type': 'array', 'items': 'float'} |
| tol_quad | Quadratic tolerance term for determining if fit is linear | Input | float | float |
| slope_min | Min slope cut off | Input | float | float |
| slope_max | Max slope cut off | Input | float | float |
| success | Whether fit was successful or not | Output | boolean | boolean |
