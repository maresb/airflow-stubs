import logging
from _typeshed import Incomplete
from airflow import settings as settings
from airflow.utils import timezone as timezone
from airflow.utils.helpers import parse_template_string as parse_template_string
from airflow.utils.log.logging_mixin import DISABLE_PROPOGATE as DISABLE_PROPOGATE
from airflow.utils.log.non_caching_file_handler import NonCachingFileHandler as NonCachingFileHandler

logger: Incomplete

class FileProcessorHandler(logging.Handler):
    handler: Incomplete
    base_log_folder: Incomplete
    dag_dir: Incomplete
    def __init__(self, base_log_folder, filename_template) -> None: ...
    def set_context(self, filename): ...
    def emit(self, record) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
