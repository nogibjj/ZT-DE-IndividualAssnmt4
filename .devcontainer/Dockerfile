# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory.
WORKDIR /code

# Install dependencies.
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project.
COPY . /code/

# Command to run the application.
CMD ["flask", "run", "--host=0.0.0.0"]
