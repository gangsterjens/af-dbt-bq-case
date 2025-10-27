# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files, including credentials
COPY . .

# Set env vars for BigQuery auth
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/Data/creds/dn-case-476208-b05c98ae2260.json"
ENV PYTHONUNBUFFERED=1

CMD ["python", "handler.py", "all"]
