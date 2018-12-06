FROM python:3.6.2
LABEL maintainer ZhuMon
ENV PYTHONUNBUFFERED 1
WORKDIR /app/.
RUN apt-get install libgraphviz-dev \
pkg-config
RUN apt-get install python3-pip
RUN pip3.6 install --upgrade pip
RUN pip3.6 install -r requirements.txt
