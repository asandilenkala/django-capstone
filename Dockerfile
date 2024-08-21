# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . .

# Set environment variables (e.g., for Django)
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=myproject.settings \
    DJANGO_ENV=production



# Expose the port the app runs on
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py"]
