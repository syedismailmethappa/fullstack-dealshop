"""Gunicorn configuration file"""

import os

# Logging
accesslog = '-'  # stdout
errorlog = '-'   # stderr
loglevel = 'info'

# Worker processes
# For Render's small containers, reduce concurrency to avoid memory/CPU exhaustion.
# Render typically assigns 1 CPU; each UvicornWorker + threads can use ~100-200MB.
# Adjust based on your container size.
workers = int(os.environ.get('WEB_CONCURRENCY', '1'))  # Default to 1 worker
worker_class = 'uvicorn.workers.UvicornWorker'
threads = 1  # Reduce threads per worker to minimize memory footprint

# Timeouts
timeout = 30
graceful_timeout = 20
keepalive = 5

# Reduce memory usage
max_requests = 1000
max_requests_jitter = 50

# Server mechanics
preload_app = False
reload = False  # Don't reload in production

# Server socket - read port from environment safely
PORT = os.environ.get('PORT', '8000')
bind = f'0.0.0.0:{PORT}'

def on_starting(server):
    """Log when server starts"""
    server.log.info('Starting server process')

def on_exit(server):
    """Log when server exits"""
    server.log.info('Shutting down server process')