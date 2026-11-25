FROM ubuntu:24.04

# Install basic tools the AI will need
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    vim \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
