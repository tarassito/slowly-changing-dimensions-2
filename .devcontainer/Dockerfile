FROM python:3.12.3-slim

RUN apt-get update && apt-get install -y --no-install-recommends \ 
    openjdk-17-jdk-headless \ 
    git \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/*

ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --no-cache-dir pyspark==3.4.4 delta-spark==2.4.0 ipykernel

