# Use an appropriate base image (e.g., Ubuntu)
FROM python:3.8

# Install PostgreSQL client
RUN apt-get update && \
    apt-get install -y postgresql-client

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django application
COPY . /app/

# Set execute permission for entrypoint script
RUN chmod +x entrypoint.sh

# Expose port 8000 (for development, adjust as needed)
EXPOSE 8000

# Command to run the entrypoint script
CMD ["./entrypoint.sh"]