# Build:  docker build -t faker-file-test .
# Test:   docker run --rm faker-file-test
# Env:    docker run --rm faker-file-test -e py311-django42-pathy0110
# Shell:  docker run --rm -it --entrypoint bash faker-file-test

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# System dependencies matching GitHub CI (ubuntu-22.04).
# default-jre-headless is required by tika (used in data-integrity tests);
# GitHub-hosted runners have Java pre-installed.
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wkhtmltopdf \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    poppler-utils \
    default-jre-headless \
    build-essential \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Point Python's SSL module to the system CA bundle.
# python-build-standalone (installed by uv) may not locate it automatically.
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# Copy uv binary from the official uv image (avoids network installer issues)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Install all Python versions used in the test matrix
RUN uv python install 3.9 3.10 3.11 3.12 3.13

# Install tox and tox-uv into a uv-managed tool environment
RUN uv tool install tox --with tox-uv

# Make uv tool binaries (tox) available on PATH
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app
COPY . .

# Pre-create directories required by tests
RUN mkdir -p examples/django_example/project/media/ \
             examples/django_example/project/static/

ENTRYPOINT ["tox"]
CMD []
