from __future__ import absolute_import
import os
from celery import Celery

app = Celery('app',
             include=['app.tasks'])

# Set default configuration module name
os.environ.setdefault('CELERY_CONFIG_MODULE', 'app.celeryconfig')

app.config_from_envvar('CELERY_CONFIG_MODULE')
# app.conf.update(
#     CELERYBEAT_SCHEDULE={
#         # Execute every three hours: midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm.
#         'check_rd_ready_to_be_preprocessed': {
#             'task': 'presta.app.tasks.check_rd_ready_to_be_preprocessed',
#             #'schedule': crontab(minute=0, hour='*/3'),
#             'schedule': crontab(minute='*/1'),
#             'kwargs': dict(),
#         },
#     }
# )

if __name__ == '__main__':
    app.start()
