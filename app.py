from main import app

# This file is needed for gunicorn to find the FastAPI app
# Run with: gunicorn app:app -k uvicorn.workers.UvicornWorker