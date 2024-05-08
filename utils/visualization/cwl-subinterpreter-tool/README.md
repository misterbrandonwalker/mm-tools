# cwl_subinterpreter (0.1.0)

Speculatively executes an arbitrary CommandLineTool (upto max_times) by file watching / polling --cachedir. This is primarily intended for parsing logfiles before the associated CWL process has finished.

## Options

This plugin takes 7 input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| cachedir_path | The full absolute path to the --cachedir cwltool directory. You should also use this same directory when invoking RealtimePlots.py,  | Input | string | string |
| file_pattern | Filenames that match this pattern will be watched / polled for changes. i.e. '*.log',  | Input | string | string |
| cwl_tool | The filename (without .cwl extension) of the CommandLineTool to speculatively execute.,  | Input | string | string |
| max_times | The maximum number of times to speculatively execute cwl_tool. This is used to guarantee termination in case of errors.,  | Input | string | string |
| config | A JSON-encoded string which contains the arguments (i.e. the `in:` tag) to the wrapped CommandLineTool. Make sure to escape any substrings as necessary! | Input | string | string |
| root_workflow_yml_path | The full absolute path to the root workflow yml file.,  | Input | string | string |
| homedir | The full absolute path to the root users home directory.,  | Input | string | string |
| output_log_path | Path to the output log file | Output | File | File |
