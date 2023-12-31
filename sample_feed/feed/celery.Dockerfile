# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y procps

# Set work directory
WORKDIR /ltp/sample_feed

# Install dependencies
COPY requirements.txt /ltp/sample_feed/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /ltp/sample_feed