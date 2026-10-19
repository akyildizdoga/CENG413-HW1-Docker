# CENG413 HW1 - Student Task Manager
# Dockerfile for a small Flask web application

FROM python:3.12.12-slim-bookworm

WORKDIR /app

# Install dependencies before copying application code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Create a non-root user
RUN useradd --create-home --uid 10001 appuser

USER appuser

# Default configuration
ENV APP_GREETING=Hello
ENV APP_ENV=production
ENV PORT=8080

EXPOSE 8080

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
