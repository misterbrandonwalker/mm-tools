#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/obmin-tool:${version}
