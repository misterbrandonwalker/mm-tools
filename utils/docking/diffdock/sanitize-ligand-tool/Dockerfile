# docker build -f Dockerfile -t polusai/sanitize-ligand-tool .

FROM python:3.11-buster

# environment variables defined
ENV EXEC_DIR="/opt/executables"

RUN mkdir -p ${EXEC_DIR}
COPY pyproject.toml ${EXEC_DIR}
COPY VERSION ${EXEC_DIR}
COPY README.md ${EXEC_DIR}
COPY CHANGELOG.md ${EXEC_DIR}
# need copy src here because pyproject.toml has a reference to the src directory
COPY src ${EXEC_DIR}/src

WORKDIR ${EXEC_DIR}

ADD Dockerfile ${EXEC_DIR}

RUN pip3 install ${EXEC_DIR} --no-cache-dir
