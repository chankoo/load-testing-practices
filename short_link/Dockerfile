FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y procps


WORKDIR /ltp/short_link

COPY requirements.txt /ltp/short_link/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /ltp/short_link