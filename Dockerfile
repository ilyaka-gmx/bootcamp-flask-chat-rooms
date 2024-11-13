FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY python-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY python-app/ .

CMD ["python", "app.py"]