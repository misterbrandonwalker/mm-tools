#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/pdbbind-refined-v2020-tool:${version}
