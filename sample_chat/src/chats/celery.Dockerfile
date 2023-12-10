# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y procps gcc libpq-dev

# Set work directory
WORKDIR /ltp/sample_chat

# Install dependencies
COPY requirements.txt /ltp/sample_chat/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy project
COPY . /ltp/sample_chat