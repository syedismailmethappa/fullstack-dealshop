"""Gunicorn configuration file"""

# Logging
accesslog = '-'  # stdout
errorlog = '-'   # stderr
loglevel = 'info'

# Worker processes
workers = 2  # Number of worker processes
worker_class = 'uvicorn.workers.UvicornWorker'
threads = 4

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

# Server socket
bind = '0.0.0.0:$PORT'  # Render will replace $PORT

def on_starting(server):
    """Log when server starts"""
    server.log.info('Starting server process')

def on_exit(server):
    """Log when server exits"""
    server.log.info('Shutting down server process')