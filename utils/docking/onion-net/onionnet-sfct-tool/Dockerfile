# docker build -f Dockerfile -t polusai/onionnet-sfct-tool .
FROM condaforge/mambaforge

RUN apt-get update && apt-get install -y wget git

RUN mamba install -c conda-forge openbabel numpy pandas mdtraj biopandas -y

# Scikit-learn 1.0.2 is only compatible with 3.6 < python < 3.11
RUN mamba install -y python=3.10

# model saved required scikit-learn==1.0.2
RUN pip install -U scikit-learn==1.0.2 rdkit-pypi

RUN git clone https://github.com/zhenglz/OnionNet-SFCT.git

WORKDIR /OnionNet-SFCT

RUN mkdir -p data && cd data && wget -nv --no-clobber https://huggingface.co/cyangNYU/OnionNet-SFCT-final-model/resolve/main/sfct_std_final.model

ADD Dockerfile .

CMD ["--help"]
