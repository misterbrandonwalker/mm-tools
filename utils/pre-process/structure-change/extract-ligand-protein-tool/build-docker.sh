#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/extract-ligand-protein-tool:${version}
