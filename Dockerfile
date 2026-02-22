FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
# Ensure uv-installed pythons are in the path if needed
ENV PATH="/root/.local/bin/:${PATH}"

# 1. Install ONLY system-level tools and libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    git \
    make \
    # faker-file specific system dependencies
    wkhtmltopdf \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    poppler-utils \
    libmagic1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Pre-fetch the Python versions we need 
# This makes the 'docker build' step contain the pythons, 
# so 'docker run' remains fast.
RUN uv python install 3.9 3.10 3.11 3.12 3.13

# 4. Install tox and tox-uv into a global-like tool space
RUN uv tool install tox --with tox-uv

WORKDIR /app
COPY . /app

# The entrypoint will now use the uv-installed tox
ENTRYPOINT ["uvx", "tox"]
