#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/sanitize-ligand-tool:${version}
