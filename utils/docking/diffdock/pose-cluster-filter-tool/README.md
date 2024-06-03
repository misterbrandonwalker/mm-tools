# pose_cluster_filter (0.1.0)

Cluster poses in protein and take max confident pose for each cluster

## Options

This plugin takes     2     input arguments and 1 output argument:

| Name          | Description             | I/O    | Type   | Default |
|---------------|-------------------------|--------|--------|---------|
| centroid_cutoff | Centroid cutoff distance to cluster ligands  | Input | float | float |
| predicted_poses | Input list of poses to be filtered | Input | File[] | File[] |
| filtered_poses | Output list of poses | Output | File[] | File[] |
