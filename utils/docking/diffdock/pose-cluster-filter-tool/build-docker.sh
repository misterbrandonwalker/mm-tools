#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/pose-cluster-filter-tool:${version}
