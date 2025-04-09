from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.executors.base_executor import BaseExecutor as BaseExecutor
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.listeners.listener import get_listener_manager as get_listener_manager
from airflow.models.base import Base as Base, ID_LEN as ID_LEN
from airflow.serialization.pydantic.job import JobPydantic as JobPydantic
from airflow.stats import Stats as Stats
from airflow.traces.tracer import Trace as Trace, span as span
from airflow.utils import timezone as timezone
from airflow.utils.helpers import convert_camel_to_snake as convert_camel_to_snake
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.platform import getuser as getuser
from airflow.utils.retries import retry_db_transaction as retry_db_transaction
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from airflow.utils.state import JobState as JobState
from functools import cached_property as cached_property
from sqlalchemy.orm.session import Session as Session
from typing import Callable, NoReturn

def health_check_threshold(job_type: str, heartrate: int) -> int | float: ...

class Job(Base, LoggingMixin):
    __tablename__: str
    id: Incomplete
    dag_id: Incomplete
    state: Incomplete
    job_type: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    latest_heartbeat: Incomplete
    executor_class: Incomplete
    hostname: Incomplete
    unixname: Incomplete
    __table_args__: Incomplete
    task_instances_enqueued: Incomplete
    dag_runs: Incomplete
    heartbeat_failed: bool
    previous_heartbeat: Incomplete
    max_tis_per_query: int
    def __init__(self, executor: BaseExecutor | None = None, heartrate: Incomplete | None = None, **kwargs) -> None: ...
    @cached_property
    def executor(self): ...
    @cached_property
    def executors(self): ...
    @cached_property
    def heartrate(self) -> float: ...
    def is_alive(self) -> bool: ...
    def kill(self, session: Session = ...) -> NoReturn: ...
    def on_kill(self) -> None: ...
    def heartbeat(self, heartbeat_callback: Callable[[Session], None], session: Session = ...) -> None: ...
    def prepare_for_execution(self, session: Session = ...): ...
    def complete_execution(self, session: Session = ...): ...
    def most_recent_job(self, session: Session = ...) -> Job | JobPydantic | None: ...

def most_recent_job(job_type: str, session: Session = ...) -> Job | JobPydantic | None: ...
def run_job(job: Job, execute_callable: Callable[[], int | None], session: Session = ...) -> int | None: ...
def execute_job(job: Job, execute_callable: Callable[[], int | None]) -> int | None: ...
def perform_heartbeat(job: Job, heartbeat_callback: Callable[[Session], None], only_if_necessary: bool) -> None: ...
