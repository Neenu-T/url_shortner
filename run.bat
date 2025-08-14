docker build -t url_shortner .
docker run -p 8000:8000 url_shortner
ngrok http 8000

