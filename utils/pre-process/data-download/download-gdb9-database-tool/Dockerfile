# docker build -f Dockerfile -t polusai/molgan-tool:0.1.0 .
FROM condaforge/mambaforge
# NOT mambaforge-pypy3 (rdkit is incompatible with pypy)

# RDKIT logging
ENV RDKIT_ERROR_LOGGING="OFF"

RUN apt-get update && apt-get install -y wget git

# Clone MolGAN
RUN git clone https://github.com/ndonyapour/MolGAN.git

# Build and install python bindings
# MolGAN was initially implemented using TensorFlow v1, and TensorFlow version 2 offers support
# for v1 functionalities. However, it's important to mention that the current patch for upgrading
# to v2 is not truly upgrading v1 API to v2 API, but calling legacy v1 API from v2 package via
# "tf.compat.v1". Essentially, it’s still v1.certain. Truely upgrade to v2 requires rewriting most
# functions of MolGAN, including model creation, data processing, and training.

RUN mamba install -c conda-forge rdkit "tensorflow<2.13" numpy scikit-learn xorg-libxrender

# Make sure rdkit is activated
RUN python -c "import rdkit"

# Train a Model
WORKDIR /MolGAN

# Download the gdb9 database
RUN bash data/download_dataset.sh data/gdb9.sdf data/NP_score.pkl.gz data/SA_score.pkl.gz

# Download the pretrained model
RUN wget -nv --no-clobber https://huggingface.co/ndonyapour/MolGAN/resolve/main/MolGAN_model.tar.gz && tar xvzf MolGAN_model.tar.gz
RUN mv MolGAN_model trained_models
RUN  wget -nv --no-clobber https://huggingface.co/ndonyapour/MolGAN/resolve/main/data.pkl -O data/data.pkl
ADD Dockerfile .
