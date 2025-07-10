FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev

# Copy files
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "wsgi.py"]
