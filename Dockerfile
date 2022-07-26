FROM debian:buster-slim

WORKDIR /app

COPY ./a.txt /app

RUN apt-get update && \
    apt-get -y install sl

CMD cat /app/a.txt