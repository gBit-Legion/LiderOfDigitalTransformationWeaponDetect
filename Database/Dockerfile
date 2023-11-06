FROM postgres:latest
ENV POSTGRES_PASSWORD=123
RUN apt-get update && apt-get upgrade -y
RUN apt-get install locales-all
COPY ./init.sql/ docker-entrypoint-initdb.d/
