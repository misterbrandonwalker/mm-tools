# docker build -f Dockerfile -t polusai/pdbfixer-tool .

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
# errors installing pdbfixer from poetry so using conda
COPY environment.yml ${EXEC_DIR}
RUN mamba env create -f ${EXEC_DIR}/environment.yml
RUN echo "source activate project_env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

COPY src ${EXEC_DIR}/src

ADD Dockerfile .

RUN conda run -n project_env pip install ${EXEC_DIR} --no-cache-dir

CMD ["--help"]
