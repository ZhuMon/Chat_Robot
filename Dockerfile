FROM python:3.6.2
LABEL maintainer ZhuMon
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api/
RUN apt-get install graphviz \
    libgraphviz-dev \
    pkg-config \
    protobuf-compiler
RUN pip install -r requirements.txt
