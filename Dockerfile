FROM python:3.9.20-slim

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Copy and install Python dependencies
COPY ./python-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY ./python-app .

# Expose port
EXPOSE 5000

# Run the application
CMD [ "python", "./app.py" ]