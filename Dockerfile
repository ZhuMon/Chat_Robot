FROM python:3.6.2
LABEL maintainer ZhuMon
ENV PYTHONUNBUFFERED 1
RUN apt-get install libgraphviz-dev \
pkg-config
RUN pip install -r requirements.txt
