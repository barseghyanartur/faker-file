# Use the official uv image to grab the binary
FROM ghcr.io/astral-sh/uv:latest AS uv_bin

FROM ubuntu:24.04

# 1. Setup Environment
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    # Ensure uv-installed binaries and the venv are in the PATH
    PATH="/workspace/.venv/bin:/root/.local/bin:$PATH"

# 2. Install System Dependencies
# Note: I removed the build-libs (libssl-dev, etc.) unless you need them 
# for compiling specific python packages later.
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    wkhtmltopdf \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    poppler-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 3. Install uv
COPY --from=uv_bin /uv /uvx /bin/

# 4. Install Python & Setup Project
WORKDIR /workspace

ARG PYTHON_VERSION=3.12
# 'uv python install' fetches a pre-compiled binary—no more 10-minute waits
RUN uv python install ${PYTHON_VERSION}

# Create the virtual environment in the workspace
RUN uv venv .venv --python ${PYTHON_VERSION}

# 5. Finalize
# Any subsequent RUN commands or the CMD will now use the .venv's Python
CMD ["/bin/bash"]
