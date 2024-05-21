# docker build -f Dockerfile -t polusai/pdbfixer-tool:0.1.0 .

FROM condaforge/mambaforge
# pdbfixer not installable with poetry

ENV EXEC_DIR="/opt/executables"
ENV POLUS_LOG="INFO"
RUN mkdir -p ${EXEC_DIR}

# Work directory defined in the base container
# WORKDIR ${EXEC_DIR}

COPY pyproject.toml ${EXEC_DIR}
COPY VERSION ${EXEC_DIR}
COPY README.md ${EXEC_DIR}
COPY CHANGELOG.md ${EXEC_DIR}
COPY src ${EXEC_DIR}/src
WORKDIR ${EXEC_DIR}

# Install needed packages here
RUN mamba install -c conda-forge pdbfixer

RUN pip3 install ${EXEC_DIR} --no-cache-dir

CMD ["--help"]
