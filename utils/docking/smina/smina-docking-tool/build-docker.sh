#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/smina-docking-tool:${version}
