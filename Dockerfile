# adapted from https://www.loopwerk.io/articles/2025/coolify-django/
FROM  debian:bookworm-slim
WORKDIR /app

# Arguments needed at build-time, to be provided by Coolify
ARG SECRET_KEY
ARG DATABASE_URI

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl wget \
    && rm -rf /var/lib/apt/lists/*

# Install uv, the fast Python package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Copy only the dependency definitions first to leverage Docker's layer caching
COPY pyproject.toml uv.lock .python-version ./

# Install Python dependencies for production
RUN uv sync --no-group dev --group prod

# Copy the rest of the application code into the container
COPY . .

# Expose the port Gunicorn will run on
EXPOSE 3000

# Run with gunicorn
CMD ["uv", "run", "--no-sync", "gunicorn", "--bind", "0.0.0.0:3000", "--workers", "3", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info", "config.wsgi:application"]