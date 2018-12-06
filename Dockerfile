FROM python:3.6.2
LABEL maintainer ZhuMon
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
COPY requirements.txt /docker_api
COPY . /docker_api/
WORKDIR /docker_api

RUN apt-get install libgraphviz-dev \
pkg-config
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python app.py runserver 0.0.0.0:$PORT
