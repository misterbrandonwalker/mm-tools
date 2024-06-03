#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/random-subset-rows-tool:${version}
