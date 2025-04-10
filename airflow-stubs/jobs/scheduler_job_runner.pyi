import logging
from _typeshed import Incomplete
from airflow import settings as settings
from airflow.callbacks.callback_requests import DagCallbackRequest as DagCallbackRequest, SlaCallbackRequest as SlaCallbackRequest, TaskCallbackRequest as TaskCallbackRequest
from airflow.callbacks.pipe_callback_sink import PipeCallbackSink as PipeCallbackSink
from airflow.configuration import conf as conf
from airflow.dag_processing.manager import DagFileProcessorAgent as DagFileProcessorAgent
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning, UnknownExecutorException as UnknownExecutorException
from airflow.executors.base_executor import BaseExecutor as BaseExecutor
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.executors.executor_utils import ExecutorName as ExecutorName
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import Job as Job, perform_heartbeat as perform_heartbeat
from airflow.models import Log as Log
from airflow.models.dag import DAG as DAG, DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.dataset import DagScheduleDatasetReference as DagScheduleDatasetReference, DatasetDagRunQueue as DatasetDagRunQueue, DatasetEvent as DatasetEvent, DatasetModel as DatasetModel, TaskOutletDatasetReference as TaskOutletDatasetReference
from airflow.models.serialized_dag import SerializedDagModel as SerializedDagModel
from airflow.models.taskinstance import SimpleTaskInstance as SimpleTaskInstance, TaskInstance as TaskInstance, TaskInstanceKey as TaskInstanceKey
from airflow.stats import Stats as Stats
from airflow.ti_deps.dependencies_states import EXECUTION_STATES as EXECUTION_STATES
from airflow.timetables.simple import DatasetTriggeredTimetable as DatasetTriggeredTimetable
from airflow.traces.tracer import Trace as Trace, span as span
from airflow.utils import timezone as timezone
from airflow.utils.dates import datetime_to_nano as datetime_to_nano
from airflow.utils.event_scheduler import EventScheduler as EventScheduler
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.retries import MAX_DB_RETRIES as MAX_DB_RETRIES, retry_db_transaction as retry_db_transaction, run_with_db_retries as run_with_db_retries
from airflow.utils.session import NEW_SESSION as NEW_SESSION, create_session as create_session, provide_session as provide_session
from airflow.utils.sqlalchemy import CommitProhibitorGuard as CommitProhibitorGuard, is_lock_not_available_error as is_lock_not_available_error, prohibit_commit as prohibit_commit, tuple_in_condition as tuple_in_condition, with_row_locks as with_row_locks
from airflow.utils.state import DagRunState as DagRunState, JobState as JobState, State as State, TaskInstanceState as TaskInstanceState
from airflow.utils.types import DagRunType as DagRunType
from dataclasses import dataclass
from sqlalchemy.engine import Result as Result
from sqlalchemy.orm import Query as Query, Session as Session

TI = TaskInstance
DR = DagRun
DM = DagModel
TASK_STUCK_IN_QUEUED_RESCHEDULE_EVENT: str

@dataclass
class ConcurrencyMap:
    dag_active_tasks_map: dict[str, int]
    task_concurrency_map: dict[tuple[str, str], int]
    task_dagrun_concurrency_map: dict[tuple[str, str, str], int]
    @classmethod
    def from_concurrency_map(cls, mapping: dict[tuple[str, str, str], int]) -> ConcurrencyMap: ...

class SchedulerJobRunner(BaseJobRunner, LoggingMixin):
    job_type: str
    subdir: Incomplete
    num_runs: Incomplete
    num_times_parse_dags: Incomplete
    do_pickle: Incomplete
    using_sqlite: Incomplete
    processor_agent: DagFileProcessorAgent | None
    dagbag: Incomplete
    def __init__(self, job: Job, subdir: str = ..., num_runs: int = ..., num_times_parse_dags: int = -1, scheduler_idle_sleep_time: float = ..., do_pickle: bool = False, log: logging.Logger | None = None, processor_poll_interval: float | None = None) -> None: ...
    def heartbeat_callback(self, session: Session = ...) -> None: ...
    def register_signals(self) -> None: ...
    def adopt_or_reset_orphaned_tasks(self, session: Session = ...) -> int: ...
    def check_trigger_timeouts(self, max_retries: int = ..., session: Session = ...) -> None: ...
