# To build:
# > docker build -f Dockerfile .
FROM docker.io/ubuntu:18.04
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install tzdata -y --no-install-recommends
RUN apt install -y git nano mc apt-utils software-properties-common --no-install-recommends
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update && apt install -y python3.6 python3.7 python3.8 python3.9 python3.10 python3-pip python3-setuptools --no-install-recommends

ENTRYPOINT  ["tail", "-f", "/dev/null"]
