# Use the official Python image from the Docker Hub
FROM python:3.10.0-slim-buster

# Upgrade pip to the latest version and install dependencies in one RUN command
RUN apt-get update && \
    apt-get install -y git libgl1-mesa-glx libglib2.0-0 && \
    python -m pip install --upgrade pip setuptools wheel && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory for output within the application directory
RUN mkdir -p /app/output && \
    chmod -R 777 /app/output  # Adjust permissions as needed

# Copy the current directory contents into the container at /app
COPY . .

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Define environment variable (if needed)
# ENV FLASK_APP=app.py

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
