#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/pdbfixer-tool:${version}
