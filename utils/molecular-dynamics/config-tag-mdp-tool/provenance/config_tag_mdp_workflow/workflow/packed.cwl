{
    "$graph": [
        {
            "steps": [
                {
                    "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0",
                    "in": [
                        {
                            "source": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___config",
                            "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/config"
                        },
                        {
                            "source": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___dt",
                            "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/dt"
                        },
                        {
                            "source": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___nsteps",
                            "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/nsteps"
                        },
                        {
                            "source": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___ref_p",
                            "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/ref_p"
                        },
                        {
                            "source": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___ref_t",
                            "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/ref_t"
                        }
                    ],
                    "out": [
                        "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/output_config_string"
                    ],
                    "run": "#config_tag_mdp_0@1@0.cwl"
                }
            ],
            "class": "Workflow",
            "inputs": [
                {
                    "type": "string",
                    "format": "https://edamontology.org/format_2330",
                    "label": "A dictionary of the given arguments as a JSON-encoded string.",
                    "doc": "A dictionary of the given arguments as a JSON-encoded string.",
                    "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___config"
                },
                {
                    "type": "float",
                    "label": "The length of each timestep",
                    "doc": "The length of each timestep",
                    "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___dt"
                },
                {
                    "type": "int",
                    "label": "The number of timesteps",
                    "doc": "The number of timesteps",
                    "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___nsteps"
                },
                {
                    "type": "float",
                    "label": "The nominal pressure",
                    "doc": "The nominal pressure",
                    "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___ref_p"
                },
                {
                    "type": "float",
                    "label": "The nominal temperature",
                    "doc": "The nominal temperature",
                    "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___ref_t"
                }
            ],
            "id": "#main",
            "outputs": [
                {
                    "type": "string",
                    "label": "A dictionary of the given arguments as a JSON-encoded string.",
                    "doc": "A dictionary of the given arguments as a JSON-encoded string.",
                    "outputSource": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/output_config_string",
                    "id": "#main/config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___output_config_string"
                }
            ]
        },
        {
            "class": "CommandLineTool",
            "label": "Returns a dictionary of the given arguments as a JSON-encoded string.",
            "doc": "Returns a dictionary of the given arguments as a JSON-encoded string.",
            "baseCommand": "echo",
            "requirements": [
                {
                    "class": "InlineJavascriptRequirement"
                }
            ],
            "inputs": [
                {
                    "label": "A dictionary of the given arguments as a JSON-encoded string.",
                    "doc": "A dictionary of the given arguments as a JSON-encoded string.",
                    "type": "string",
                    "format": "https://edamontology.org/format_2330",
                    "default": "{}",
                    "id": "#config_tag_mdp_0@1@0.cwl/config"
                },
                {
                    "label": "The length of each timestep",
                    "doc": "The length of each timestep",
                    "type": "float",
                    "id": "#config_tag_mdp_0@1@0.cwl/dt"
                },
                {
                    "label": "The number of timesteps",
                    "doc": "The number of timesteps",
                    "type": "int",
                    "id": "#config_tag_mdp_0@1@0.cwl/nsteps"
                },
                {
                    "label": "The nominal pressure",
                    "doc": "The nominal pressure",
                    "type": "float",
                    "id": "#config_tag_mdp_0@1@0.cwl/ref_p"
                },
                {
                    "label": "The nominal temperature",
                    "doc": "The nominal temperature",
                    "type": "float",
                    "id": "#config_tag_mdp_0@1@0.cwl/ref_t"
                }
            ],
            "outputs": [
                {
                    "label": "A dictionary of the given arguments as a JSON-encoded string.",
                    "doc": "A dictionary of the given arguments as a JSON-encoded string.",
                    "type": "string",
                    "outputBinding": {
                        "outputEval": "${\n  var config = JSON.parse(inputs.config);\n  if ((\"mdp\" in config) === false) {\n    config[\"mdp\"] = {}; // Initialize it\n  }\n  // TODO: Check for duplicate keys, i.e.\n  // \"Pressure coupling incorrect number of values (I need exactly 1)\"\n  config[\"mdp\"][\"nsteps\"] = inputs.nsteps;\n  config[\"mdp\"][\"dt\"] = inputs.dt;\n  config[\"mdp\"][\"ref-t\"] = inputs[\"ref-t\"]; //Javascript interprets dash as subtract...\n  config[\"mdp\"][\"ref-p\"] = inputs[\"ref-p\"];\n  return JSON.stringify(config);\n}\n"
                    },
                    "id": "#config_tag_mdp_0@1@0.cwl/output_config_string"
                }
            ],
            "id": "#config_tag_mdp_0@1@0.cwl",
            "hints": [
                {
                    "class": "LoadListingRequirement",
                    "loadListing": "deep_listing"
                },
                {
                    "class": "NetworkAccess",
                    "networkAccess": true
                }
            ]
        }
    ],
    "cwlVersion": "v1.2",
    "$schemas": [
        "https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl"
    ],
    "$namespaces": {
        "edam": "https://edamontology.org/"
    }
}
