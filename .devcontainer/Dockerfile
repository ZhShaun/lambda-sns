FROM mcr.microsoft.com/devcontainers/base:ubuntu

USER vscode

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# install github action act
RUN curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# install brew
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
ENV PATH="/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:${PATH}"

RUN brew install pinact

RUN brew install localstack/tap/localstack-cli
