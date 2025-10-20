# Stage 1: Build the frontend assets
FROM node:20 AS frontend
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY tailwind.config.js .
COPY app/static/src/input.css app/static/src/input.css
RUN npm install -g @tailwindcss/cli
RUN tailwindcss -i app/static/src/input.css -o app/static/dist/style.css

# Stage 2: Create the final Python application
FROM python:3.12-slim
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Copy the built frontend assets from the frontend stage
COPY --from=frontend /app/app/static/dist/style.css app/static/dist/style.css

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP main:app

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "main:app"]
