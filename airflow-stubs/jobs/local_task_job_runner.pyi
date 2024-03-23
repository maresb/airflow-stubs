import airflow.jobs.base_job_runner
import airflow.utils.log.logging_mixin
import airflow.utils.timezone as timezone
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import perform_heartbeat as perform_heartbeat
from airflow.models.taskinstance import TaskReturnCode as TaskReturnCode
from airflow.stats import Stats as Stats
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from typing import ClassVar

TYPE_CHECKING: bool
IS_WINDOWS: bool
NEW_SESSION: None
SIGSEGV_MESSAGE: str

class LocalTaskJobRunner(airflow.jobs.base_job_runner.BaseJobRunner, airflow.utils.log.logging_mixin.LoggingMixin):
    job_type: ClassVar[str] = ...
    def __init__(self, job: Job, task_instance: TaskInstance | TaskInstancePydantic, ignore_all_deps: bool = ..., ignore_depends_on_past: bool = ..., wait_for_past_depends_before_skipping: bool = ..., ignore_task_deps: bool = ..., ignore_ti_state: bool = ..., mark_success: bool = ..., pickle_id: int | None = ..., pool: str | None = ..., external_executor_id: str | None = ...) -> None: ...
    def handle_task_exit(self, return_code: int) -> None: ...
    def on_kill(self): ...
    def heartbeat_callback(self, *args, **kwargs) -> None: ...
