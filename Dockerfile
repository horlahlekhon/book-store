FROM ubuntu:latest

LABEL MAINTAINER="lekan.adebari@ubanquity.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# copy requirement.txt so that docker can cache 
COPY ./requirements.txt /app/bookstore/requirements.txt 

WORKDIR /app/bookstore

RUN pip install -r requirements.txt 

COPY . /app/bookstore

ENTRYPOINT [ "python","manage.py","runserver"]

