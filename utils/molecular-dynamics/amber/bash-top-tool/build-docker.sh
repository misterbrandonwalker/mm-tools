#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/bash-top-tool:${version}
