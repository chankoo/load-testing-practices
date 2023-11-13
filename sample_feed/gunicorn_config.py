import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
worker_connection = 1000

bind = '0.0.0.0:80'
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
timeout = 30
reload = True
