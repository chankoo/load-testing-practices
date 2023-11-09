# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /ltp/sample-feed

# Install dependencies
COPY requirements.txt /ltp/sample-feed/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /ltp/sample-feed

RUN python manage.py makemigrations && python manage.py migrate

# Run the application on the specified port
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:application"]
