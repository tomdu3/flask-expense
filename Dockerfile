# Stage 1: Build the frontend assets
FROM node:20-slim AS frontend
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY tailwind.config.js .
COPY app/static/src/input.css app/static/src/input.css
RUN npm install -g @tailwindcss/cli
RUN tailwindcss -i app/static/src/input.css -o app/static/dist/style.css --minify

# Stage 2: Create the final Python application
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

# Copy the built frontend assets from the frontend stage
COPY --from=frontend /app/app/static/dist/style.css app/static/dist/style.css

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=main:app
ENV FLASK_ENV=production

# Create non-root user
RUN useradd -m myuser
USER myuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app", "--workers", "4", "--threads", "2"]