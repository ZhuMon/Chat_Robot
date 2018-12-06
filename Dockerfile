FROM python:3.6.2
LABEL maintainer ZhuMon
ENV PYTHONUNBUFFERED 1
WORKDIR /app/.
RUN apt-get install libgraphviz-dev \
pkg-config
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

CMD python app.py runserver 0.0.0.0:$PORT
