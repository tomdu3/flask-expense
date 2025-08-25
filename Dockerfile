# Create the final Python application
FROM python:3.12-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=main:app
ENV FLASK_ENV=production

# Create non-root user
RUN useradd -m myuser
USER myuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app", "--workers", "4", "--threads", "2"]