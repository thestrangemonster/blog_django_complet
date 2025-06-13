# Dockerfile for a Django application with Gunicorn
FROM python:3-slim

# Set environment variables to avoid Python buffering and enable unbuffered output
RUN apt-get update && apt-get dist-upgrade -y

# Install system dependencies
RUN useradd -m appuser

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install Gunicorn and psycopg2-binary for PostgreSQL support
RUN pip install --no-cache-dir gunicorn psycopg2-binary

# Install additional dependencies if needed
COPY . .

# Collect static files
RUN mkdir -p /app/static

# Set environment variables
RUN chown -R appuser /app

# Set the user to run the application
USER appuser

# Expose the port the app runs on
EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0:8000"]


