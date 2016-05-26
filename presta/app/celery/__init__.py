from __future__ import absolute_import
import os
from celery import Celery

app = Celery('app',
             include=['app.celery.tasks'])

# Set default configuration module name
os.environ.setdefault('CELERY_CONFIG_MODULE', 'app.celery.celeryconfig')

app.config_from_envvar('CELERY_CONFIG_MODULE')

if __name__ == '__main__':
    app.start()
