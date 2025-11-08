#!/bin/bash
set -e

echo "--- 🚀 Starting post-create setup ---"

echo "Enabling Corepack..."
corepack enable

echo "Syncing Python dependencies with uv..."
uv sync --all-extras


echo "Installing CDK dependencies..."
cd cdk-infra
yarn install
cd ..


echo "--- ✅ Setup complete ---"
