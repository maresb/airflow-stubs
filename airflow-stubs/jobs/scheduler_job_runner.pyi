import airflow.jobs.base_job_runner
import airflow.settings as settings
import airflow.utils.log.logging_mixin
import airflow.utils.timezone as timezone
import dataclasses
import logging
from airflow.callbacks.callback_requests import DagCallbackRequest as DagCallbackRequest, SlaCallbackRequest as SlaCallbackRequest, TaskCallbackRequest as TaskCallbackRequest
from airflow.callbacks.pipe_callback_sink import PipeCallbackSink as PipeCallbackSink
from airflow.configuration import conf as conf
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import Job as Job, perform_heartbeat as perform_heartbeat
from airflow.models.dag import DAG as DAG, DM as DM, DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.dagrun import DR as DR, DagRun as DagRun
from airflow.models.dataset import DagScheduleDatasetReference as DagScheduleDatasetReference, DatasetDagRunQueue as DatasetDagRunQueue, DatasetEvent as DatasetEvent, DatasetModel as DatasetModel, TaskOutletDatasetReference as TaskOutletDatasetReference
from airflow.models.serialized_dag import SerializedDagModel as SerializedDagModel
from airflow.models.taskinstance import SimpleTaskInstance as SimpleTaskInstance, TI as TI, TaskInstance as TaskInstance
from airflow.stats import Stats as Stats
from airflow.timetables.simple import DatasetTriggeredTimetable as DatasetTriggeredTimetable
from airflow.utils.event_scheduler import EventScheduler as EventScheduler
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.log.task_context_logger import TaskContextLogger as TaskContextLogger
from airflow.utils.retries import retry_db_transaction as retry_db_transaction, run_with_db_retries as run_with_db_retries
from airflow.utils.session import create_session as create_session, provide_session as provide_session
from airflow.utils.sqlalchemy import is_lock_not_available_error as is_lock_not_available_error, prohibit_commit as prohibit_commit, skip_locked as skip_locked, tuple_in_condition as tuple_in_condition, with_row_locks as with_row_locks
from airflow.utils.state import DagRunState as DagRunState, JobState as JobState, State as State, TaskInstanceState as TaskInstanceState
from airflow.utils.types import DagRunType as DagRunType
from typing import ClassVar

TYPE_CHECKING: bool
EXECUTION_STATES: set
MAX_DB_RETRIES: int
NEW_SESSION: None

class ConcurrencyMap:
    __dataclass_params__: ClassVar[dataclasses._DataclassParams] = ...
    __dataclass_fields__: ClassVar[dict] = ...
    @classmethod
    def from_concurrency_map(cls, mapping: dict[tuple[str, str, str], int]) -> ConcurrencyMap: ...
    def __init__(self, dag_active_tasks_map: dict[str, int], task_concurrency_map: dict[tuple[str, str], int], task_dagrun_concurrency_map: dict[tuple[str, str, str], int]) -> None: ...
    def __eq__(self, other) -> bool: ...

class SchedulerJobRunner(airflow.jobs.base_job_runner.BaseJobRunner, airflow.utils.log.logging_mixin.LoggingMixin):
    job_type: ClassVar[str] = ...
    heartrate: ClassVar[int] = ...
    def __init__(self, job: Job, subdir: str = ..., num_runs: int = ..., num_times_parse_dags: int = ..., scheduler_idle_sleep_time: float = ..., do_pickle: bool = ..., log: logging.Logger | None = ..., processor_poll_interval: float | None = ...) -> None: ...
    def heartbeat_callback(self, *args, **kwargs) -> None: ...
    def register_signals(self) -> None: ...
    def adopt_or_reset_orphaned_tasks(self, *args, **kwargs) -> int: ...
    def check_trigger_timeouts(self, *args, **kwargs) -> None: ...
