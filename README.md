# ZT-DE-IndividualAssnmt4

# Auto-Scaling Flask App on Azure

## Project Overview

This project is a Flask web application designed to demonstrate auto-scaling capabilities using Azure App Services. The application features a simple interface that responds to HTTP requests with a welcome message.

## Dependencies

- Flask
- gunicorn (for WSGI HTTP Server)
- azure-storage-blob (for Azure Blob Storage interaction, if used)
- Any other libraries listed in `requirements.txt`

## How to Run

### Local Setup

1. Clone the repository:
git clone https://github.com/nogibjj/ZT-DE-IndividualAssnmt4

2. Navigate to the repo directory:
cd ZT-DE-IndividualAssnmt4

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
python app.py


### Running with Docker

1. Build the Docker image:
docker build -t my-flask-app .

2. Run the Docker container:
docker run -p 5000:5000 my-flask-app
