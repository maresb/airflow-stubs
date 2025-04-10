from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from typing import Any

LOG_LEVEL: str
FAB_LOG_LEVEL: str
LOG_FORMAT: str
DAG_PROCESSOR_LOG_FORMAT: str
LOG_FORMATTER_CLASS: str
COLORED_LOG_FORMAT: str
COLORED_LOG: bool
COLORED_FORMATTER_CLASS: str
DAG_PROCESSOR_LOG_TARGET: str
BASE_LOG_FOLDER: str
PROCESSOR_LOG_FOLDER: str
DAG_PROCESSOR_MANAGER_LOG_LOCATION: str
DAG_PROCESSOR_MANAGER_LOG_STDOUT: str
FILENAME_TEMPLATE: str | None
PROCESSOR_FILENAME_TEMPLATE: str
DEFAULT_LOGGING_CONFIG: dict[str, Any]
EXTRA_LOGGER_NAMES: str | None
new_loggers: Incomplete
DEFAULT_DAG_PARSING_LOGGING_CONFIG: dict[str, dict[str, dict[str, Any]]]
processor_manager_handler_config: dict[str, Any]
directory: str
REMOTE_LOGGING: bool
ELASTICSEARCH_HOST: str | None
REMOTE_BASE_LOG_FOLDER: str
REMOTE_TASK_HANDLER_KWARGS: Incomplete
S3_REMOTE_HANDLERS: dict[str, dict[str, str | None]]
url_parts: Incomplete
CLOUDWATCH_REMOTE_HANDLERS: dict[str, dict[str, str | None]]
key_path: Incomplete
GCS_REMOTE_HANDLERS: dict[str, dict[str, str | None]]
wasb_log_container: Incomplete
WASB_REMOTE_HANDLERS: dict[str, dict[str, str | bool | None]]
log_name: Incomplete
STACKDRIVER_REMOTE_HANDLERS: Incomplete
OSS_REMOTE_HANDLERS: Incomplete
HDFS_REMOTE_HANDLERS: dict[str, dict[str, str | None]]
ELASTICSEARCH_END_OF_LOG_MARK: str
ELASTICSEARCH_FRONTEND: str
ELASTICSEARCH_WRITE_STDOUT: bool
ELASTICSEARCH_JSON_FORMAT: bool
ELASTICSEARCH_JSON_FIELDS: str
ELASTICSEARCH_HOST_FIELD: str
ELASTICSEARCH_OFFSET_FIELD: str
ELASTIC_REMOTE_HANDLERS: dict[str, dict[str, str | bool | None]]
