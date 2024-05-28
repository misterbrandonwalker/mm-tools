#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/autodock-vina-tool:${version}
