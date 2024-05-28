# gunicorn_config.py

# Bind to a specific IP and port
bind = "0.0.0.0:8000"

# Number of worker processes
workers = 4

# The type of workers to use
worker_class = "sync"

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Timeout settings
timeout = 30
keepalive = 2
