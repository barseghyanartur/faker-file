FROM ghcr.io/astral-sh/uv:latest AS uv_bin
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    VENVS_PATH=/opt/venvs

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl git \
    wkhtmltopdf libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 poppler-utils \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=uv_bin /uv /uvx /bin/

RUN mkdir -p $VENVS_PATH

WORKDIR /workspace

ARG PYTHON_VERSION=3.12
RUN uv python install ${PYTHON_VERSION}

CMD ["/bin/bash"]
