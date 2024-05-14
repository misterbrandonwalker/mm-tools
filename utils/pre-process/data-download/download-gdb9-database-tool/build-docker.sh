
#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/molgan-tool:${version}
