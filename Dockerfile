FROM python:3.8

MAINTAINER Rixson

ENV PYTHONUNBUFFERED 1

COPY pip.conf /root/.pip/pip.conf

RUN mkdir -p /var/www/petcharm/petcharm_server

RUN apt-get update && apt-get install net-tools vim -y

WORKDIR /var/www/petcharm/petcharm_server

ADD . /var/www/petcharm/petcharm_server

RUN pip install -r requirements.txt

CMD [ "sh", "/var/www/petcharm/petcharm_server/start.sh" ]
