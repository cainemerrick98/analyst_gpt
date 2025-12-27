FROM python:3.11-slim

WORKDIR /app

# Install system deps (if needed)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy code
COPY . .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Ensure data dir exists
RUN mkdir -p /data

# Expose API port
EXPOSE 8000

# Default command = API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
