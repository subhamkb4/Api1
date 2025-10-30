# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY api.py .

# Run the script when the container starts
CMD ["python", "api.py"]
