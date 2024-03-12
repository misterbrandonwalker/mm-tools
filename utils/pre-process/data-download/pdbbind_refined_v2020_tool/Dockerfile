# docker build -f Dockerfile -t polusai/pdbbind-refined-v2020-tool .

FROM condaforge/mambaforge

ENV EXEC_DIR="/opt/executables"
ENV POLUS_LOG="INFO"
RUN mkdir -p ${EXEC_DIR}

RUN apt-get update && apt-get install -y wget
# Download the bdbbind dataset
# RUN wget --no-clobber http://www.pdbbind.org.cn/download/PDBbind_v2020_refined.tar.gz
## update to the new download URL (around 10 times faster) from PDBbind website.
RUN wget --no-clobber https://pdbbind.oss-cn-hangzhou.aliyuncs.com/download/PDBbind_v2020_refined.tar.gz
RUN tar -xvf PDBbind_v2020_refined.tar.gz

# Work directory defined in the base container

COPY pyproject.toml ${EXEC_DIR}
COPY VERSION ${EXEC_DIR}
COPY README.md ${EXEC_DIR}
COPY CHANGELOG.md ${EXEC_DIR}

# Install needed packages here
RUN mamba install -c conda-forge pandas

COPY src ${EXEC_DIR}/src

RUN pip3 install ${EXEC_DIR} --no-cache-dir

CMD ["--help"]

WORKDIR /outdir
