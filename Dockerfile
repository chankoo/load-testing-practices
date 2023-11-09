# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /load-testing-practices

# Install dependencies
COPY requirements.txt /load-testing-practices/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /load-testing-practices/

RUN python manage.py makemigrations && python manage.py migrate

# Run the application on the specified port
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:application"]
