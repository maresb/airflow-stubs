import logging
from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.executors.base_executor import BaseExecutor as BaseExecutor
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.models import DagRun as DagRun
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.serialization.pydantic.dag_run import DagRunPydantic as DagRunPydantic
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.utils.context import Context as Context
from airflow.utils.helpers import parse_template_string as parse_template_string, render_template_to_string as render_template_to_string
from airflow.utils.log.logging_mixin import SetContextPropagate as SetContextPropagate
from airflow.utils.log.non_caching_file_handler import NonCachingRotatingFileHandler as NonCachingRotatingFileHandler
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import State as State, TaskInstanceState as TaskInstanceState
from enum import Enum
from functools import cached_property as cached_property

logger: Incomplete

class LogType(str, Enum):
    TRIGGER = 'trigger'
    WORKER = 'worker'

class FileTaskHandler(logging.Handler):
    trigger_should_wrap: bool
    inherits_from_empty_operator_log_message: str
    executor_instances: dict[str, BaseExecutor]
    DEFAULT_EXECUTOR_KEY: str
    handler: logging.Handler | None
    local_base: Incomplete
    maintain_propagate: bool
    max_bytes: Incomplete
    backup_count: Incomplete
    delay: Incomplete
    ctx_task_deferred: bool
    def __init__(self, base_log_folder: str, filename_template: str | None = None, max_bytes: int = 0, backup_count: int = 0, delay: bool = False) -> None: ...
    def set_context(self, ti: TaskInstance, *, identifier: str | None = None) -> None | SetContextPropagate: ...
    @cached_property
    def supports_task_context_logging(self) -> bool: ...
    @staticmethod
    def add_triggerer_suffix(full_path, job_id: Incomplete | None = None): ...
    def emit(self, record) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def read(self, task_instance, try_number: Incomplete | None = None, metadata: Incomplete | None = None): ...
