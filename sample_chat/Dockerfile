FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y procps gcc libpq-dev


WORKDIR /ltp/sample_chat

COPY requirements.txt /ltp/sample_chat/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /ltp/sample_chat

