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

RUN mkdir /var/log/gunicorn && touch /var/log/gunicorn/access.log && touch /var/log/gunicorn/error.log

RUN python manage.py flush --noinput && find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

RUN python manage.py makemigrations && python manage.py migrate

RUN echo "from sample_feed.scripts import do_initial_gen;do_initial_gen()" | python manage.py shell
