# docker build -f Dockerfile -t polusai/torch-drug-tool .

FROM condaforge/mambaforge

ENV EXEC_DIR="/opt/executables"
ENV POLUS_LOG="INFO"
RUN mkdir -p ${EXEC_DIR}

# Install g++ and other essential packages
# needed to install torch
RUN apt-get update && apt-get install -y \
    g++ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Work directory defined in the base container
WORKDIR ${EXEC_DIR}

COPY pyproject.toml ${EXEC_DIR}
COPY VERSION ${EXEC_DIR}
COPY README.md ${EXEC_DIR}
COPY CHANGELOG.md ${EXEC_DIR}
# need this here because poetry install needs the src directory
COPY src ${EXEC_DIR}/src

# Install needed packages here
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry install
# need to install torch here otherwise get
#0 2.132 Collecting torch-cluster==1.6.0 (from polus-mm-utils-torchdrug_download==0.1.0)
#0 2.144   Downloading torch_cluster-1.6.0.tar.gz (43 kB)
#0 2.150      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.4/43.4 kB 9.0 MB/s eta 0:00:00
#0 2.164   Preparing metadata (setup.py): started
#0 2.329   Preparing metadata (setup.py): finished with status 'error'
#0 2.333   error: subprocess-exited-with-error
#0 2.333
#0 2.333   × python setup.py egg_info did not run successfully.
#0 2.333   │ exit code: 1
#0 2.333   ╰─> [6 lines of output]
#0 2.333       Traceback (most recent call last):
#0 2.333         File "<string>", line 2, in <module>
#0 2.333         File "<pip-setuptools-caller>", line 34, in <module>
#0 2.333         File "/tmp/pip-install-fdght_zq/torch-cluster_10a1a1bbf63e4e1ca1e035b9639f5253/setup.py", line 8, in <module>
#0 2.333           import torch
#0 2.333       ModuleNotFoundError: No module named 'torch'
RUN pip3 install torch

RUN pip3 install ${EXEC_DIR} --no-cache-dir
