# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file first for efficient layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Default command: run FastAPI app
CMD ["python", "app/main.py", "--mode", "api"]
