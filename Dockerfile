# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install curl & unzip to download ngrok
RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*

# Download and install ngrok
RUN curl -s https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip -o ngrok.zip \
    && unzip ngrok.zip \
    && mv ngrok /usr/local/bin/ \
    && rm ngrok.zip

# Expose Django port
EXPOSE 8000
RUN ngrok authtoken 31GfFYPOp9MRIDHX7ZgdPiNU7zd_5rUnDJWcDRze1bHwMA6Wi
# Start Django and Ngrok
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000 & ngrok http 8000 --log=stdout"]

