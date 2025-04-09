from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import Job as Job, perform_heartbeat as perform_heartbeat
from airflow.models.taskinstance import TaskInstance as TaskInstance, TaskReturnCode as TaskReturnCode
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.stats import Stats as Stats
from airflow.traces.tracer import Trace as Trace
from airflow.utils import timezone as timezone
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.platform import IS_WINDOWS as IS_WINDOWS, getuser as getuser
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from sqlalchemy.orm import Session as Session

SIGSEGV_MESSAGE: str

class LocalTaskJobRunner(BaseJobRunner, LoggingMixin):
    job_type: str
    task_instance: Incomplete
    ignore_all_deps: Incomplete
    ignore_depends_on_past: Incomplete
    wait_for_past_depends_before_skipping: Incomplete
    ignore_task_deps: Incomplete
    ignore_ti_state: Incomplete
    pool: Incomplete
    pickle_id: Incomplete
    mark_success: Incomplete
    external_executor_id: Incomplete
    terminating: bool
    def __init__(self, job: Job, task_instance: TaskInstance | TaskInstancePydantic, ignore_all_deps: bool = False, ignore_depends_on_past: bool = False, wait_for_past_depends_before_skipping: bool = False, ignore_task_deps: bool = False, ignore_ti_state: bool = False, mark_success: bool = False, pickle_id: int | None = None, pool: str | None = None, external_executor_id: str | None = None) -> None: ...
    def handle_task_exit(self, return_code: int) -> None: ...
    def on_kill(self) -> None: ...
    def heartbeat_callback(self, session: Session = ...) -> None: ...
