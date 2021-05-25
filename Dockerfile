FROM artifactory.pfizer.com/vessel-core-docker-dev/vessel-core-image-ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y &&\
    apt-get install python3 -y &&\
    apt install python3-pip -y

RUN apt-get install supervisor -y
# for celery flower
EXPOSE 5679

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

COPY . /etc/supervisor/conf.d/

RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-9

CMD ["supervisord"]