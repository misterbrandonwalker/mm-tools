#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/rename-residues-mol-tool:${version}
