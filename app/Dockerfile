# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install system dependencies (PostgreSQL client tools)
RUN apt-get update && apt-get install -y postgresql-client gcc libpq-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ETL script into the container
COPY etl.py .

# Run the Python script
CMD ["python", "etl.py"]


