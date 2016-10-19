from __future__ import absolute_import

from . import app
from presta.app.events import emit_event

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


@app.task(name='presta.app.cron.check_rd_ready_to_be_preprocessed')
def check_rd_ready_to_be_preprocessed(**kwargs):
    logger.info('Cron Task: searching for run ready to be preprocessed...')
    emit_event().apply_async(event='check_rd')
    return True