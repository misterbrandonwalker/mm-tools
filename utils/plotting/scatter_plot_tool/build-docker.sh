#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/scatter-plot-tool:${version}
