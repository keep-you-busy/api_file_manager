from api.models import File

from celery import shared_task
from celery.utils.log import get_task_logger


if get_task_logger(__name__):
    logger = get_task_logger(__name__)


@shared_task
def process_file(file_id):
    try:
        file = File.objects.get(pk=file_id)
        logger.info(f"Processing file {file_id}")
        with file.file.open('r') as file_content:
            content = file_content.read()
        if content:
            file.content = content
        file.processed = True
        file.save()
    except File.DoesNotExist:
        logger.error(f"File {file_id} does not exist.")
    except Exception as error:
        logger.error(f"An error occurred with file {file_id}: {error}")
