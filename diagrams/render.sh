#!/bin/sh
set -eu
mkdir -p static/diagrams
for diagram in to-package to-user; do
  docker run --rm --user "$(id -u):$(id -g)" -v "$PWD:/data" \
    ghcr.io/mermaid-js/mermaid-cli/mermaid-cli:11.4.2@sha256:99c983b3ab4e14033f2880bc1b9de17e5090b4515dabd63fe9cf8c0ae6130956 \
    -c /data/diagrams/config.json -i "/data/diagrams/$diagram.mmd" -o "/data/static/diagrams/$diagram.svg" -b white
done
