#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/autodock-vina-run-tool:${version}
