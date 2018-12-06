FROM python:3.6.2
LABEL maintainer ZhuMon
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api/
RUN sudo apt-get install graphviz
RUN sudo apt-get install libgraphviz-dev
RUN sudo apt-get install pkg-config
RUN sudo apt-get install protobuf-compiler
RUN pip install -r requirements.txt
