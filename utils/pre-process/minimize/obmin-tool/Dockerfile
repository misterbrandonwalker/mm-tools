# docker build -f Dockerfile -t polusai/openbabel-tool .
FROM condaforge/mambaforge
# NOT mambaforge-pypy3 (openbabel is incompatible with pypy)
RUN mamba install -c conda-forge openbabel
