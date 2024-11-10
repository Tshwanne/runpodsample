FROM runpod/base:0.6.2-cpu

SHELL ["/bin/bash", "-c"]

WORKDIR /workdir

# Install missing dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils zstd python3.10-venv git-lfs unzip && \
    apt clean && rm -rf /var/lib/apt/lists/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash

# Install Python dependencies
COPY builder/requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    rm /requirements.txt


# Add src files (Worker Template)
ADD src .

CMD python -u /handler.py
