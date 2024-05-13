#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/onion-sfct-tool:${version}
