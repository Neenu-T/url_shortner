# URL Shortener Django Project

## Quick Start (Docker)

Follow these steps to run the project with a single command:

### Prerequisites
- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Setup & Run

1. **Clone the repository** (if not already done):
   ```
   git clone https://github.com/Neenu-T/url_shortner.git 
   cd url_shortner
   ```

2. **Start the app**:
   ```
   docker-compose up
   ```

   This will:
   - Build the Docker image for Django.
   - Start a PostgreSQL database.
   - Run migrations automatically.
   - Launch the Django development server.

3. **Access the app**:
   - Open [http://localhost:8000](http://localhost:8000) in your browser.
   - Anyone running the app locally can visit this URL to use the URL Shortener.

### Development

- Any changes to the code will auto-reload the Django server.
- To stop the app, press `Ctrl+C` in your terminal.

### Troubleshooting

- If you need to reset the database, run:
  ```
  docker-compose down -v
  docker-compose up --build
  ```

### Project Structure

- `Dockerfile` - Docker image for Django.
- `docker-compose.yml` - Multi-service setup (web + db).
- `requirements.txt` - Python dependencies.

---

**Enjoy!**
