FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY wealthbridge/ /app/

# Create necessary directories
RUN mkdir -p /app/data /app/staticfiles && \
    chmod 777 /app/data /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Start the application
CMD gunicorn wealthbridge.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads 2
