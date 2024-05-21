<<<<<<<< HEAD:utils/remove-terminal-residue-name-prefixes-plugin/Dockerfile
========
# docker build -f Dockerfile -t polusai/rename-residues-mol-tool:0.1.0 .
>>>>>>>> fb47176 (rename, use docker hash):utils/pre-process/structure-changes/rename-residues-mol-tool/Dockerfile
FROM condaforge/mambaforge

ENV EXEC_DIR="/opt/executables"
ENV POLUS_LOG="INFO"
RUN mkdir -p ${EXEC_DIR}


# Work directory defined in the base container
# WORKDIR ${EXEC_DIR}

COPY pyproject.toml ${EXEC_DIR}
COPY VERSION ${EXEC_DIR}
COPY README.md ${EXEC_DIR}
COPY CHANGELOG.md ${EXEC_DIR}

# Install needed packages here

COPY src ${EXEC_DIR}/src

RUN pip3 install ${EXEC_DIR} --no-cache-dir

CMD ["--help"]
