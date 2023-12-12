FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y procps

WORKDIR /ltp/id_generator

COPY requirements.txt /ltp/id_generator/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /ltp/id_generator
