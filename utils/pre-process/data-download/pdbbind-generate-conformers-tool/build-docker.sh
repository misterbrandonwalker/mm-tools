#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/pdbbind-generate-conformers-tool:${version}
