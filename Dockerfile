# -------- STAGE 1: Build Stage --------
FROM python:3.12-slim AS builder

# Install build tools and dependencies
RUN apt-get update && apt-get install -y \
    build-essential libssl-dev libffi-dev curl unzip git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python packages
COPY requirements.txt /tmp/
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

# -------- STAGE 2: Runtime Stage --------
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLY_APP_NAME=valortrustfinance
ENV DJANGO_SETTINGS_MODULE=wealthbridge.settings

WORKDIR /app

# Install runtime dependencies (SQLite support)
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the entire wealthbridge directory (which contains manage.py and your app)
COPY wealthbridge/ /app/

# Create data directory for persistent volume
RUN mkdir -p /app/data && chmod 777 /app/data

# Create static directory
RUN mkdir -p /app/staticfiles && chmod 777 /app/staticfiles

# Collect static files - now manage.py is at /app/manage.py
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "wealthbridge.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--threads", "2"]g