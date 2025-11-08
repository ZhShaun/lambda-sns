#!/bin/bash
set -e

echo "--- 🚀 Starting post-create setup ---"

echo "Enabling Corepack..."
corepack enable

echo "Installing global NPM packages..."
npm install -g @devcontainers/cli

echo "Syncing Python dependencies with uv..."
uv sync --all-extras


echo "Installing CDK dependencies..."
cd cdk-infra
yarn install
cd ..


echo "--- ✅ Setup complete ---"
