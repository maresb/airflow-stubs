import airflow.jobs.base_job_runner
import airflow.models as models
import airflow.utils.helpers as helpers
import airflow.utils.log.logging_mixin
import airflow.utils.timezone as timezone
import pendulum
from _typeshed import Incomplete
from airflow.configuration import airflow_conf as airflow_conf
from airflow.exceptions import AirflowException as AirflowException, BackfillUnfinished as BackfillUnfinished, DagConcurrencyLimitReached as DagConcurrencyLimitReached, NoAvailablePoolSlot as NoAvailablePoolSlot, PoolNotFound as PoolNotFound, TaskConcurrencyLimitReached as TaskConcurrencyLimitReached
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import Job as Job, perform_heartbeat as perform_heartbeat
from airflow.models.dag import DAG as DAG
from airflow.models.dagpickle import DagPickle as DagPickle
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.timetables.base import DagRunInfo as DagRunInfo
from airflow.utils.configuration import tmp_configuration_copy as tmp_configuration_copy
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState, State as State, TaskInstanceState as TaskInstanceState
from airflow.utils.types import DagRunType as DagRunType
from typing import ClassVar

TYPE_CHECKING: bool
BACKFILL_QUEUED_DEPS: set
NEW_SESSION: None

class BackfillJobRunner(airflow.jobs.base_job_runner.BaseJobRunner, airflow.utils.log.logging_mixin.LoggingMixin):
    class _DagRunTaskStatus:
        __attrs_attrs__: ClassVar[_DagRunTaskStatusAttributes] = ...
        __attrs_own_setattr__: ClassVar[bool] = ...
        active_runs: Incomplete
        deadlocked: Incomplete
        executed_dag_run_dates: Incomplete
        failed: Incomplete
        finished_runs: Incomplete
        not_ready: Incomplete
        running: Incomplete
        skipped: Incomplete
        succeeded: Incomplete
        to_run: Incomplete
        total_runs: Incomplete
        def __eq__(self, other) -> bool: ...
        def __ne__(self, other) -> bool: ...
        def __init__(self, to_run: dict[TaskInstanceKey, TaskInstance] = ..., running: dict[TaskInstanceKey, TaskInstance] = ..., skipped: set[TaskInstanceKey] = ..., succeeded: set[TaskInstanceKey] = ..., failed: set[TaskInstanceKey] = ..., not_ready: set[TaskInstanceKey] = ..., deadlocked: set[TaskInstance] = ..., active_runs: set[DagRun] = ..., executed_dag_run_dates: set[pendulum.DateTime] = ..., finished_runs: int = ..., total_runs: int = ...) -> None: ...
    job_type: ClassVar[str] = ...
    STATES_COUNT_AS_RUNNING: ClassVar[tuple] = ...
    def __init__(self, job: Job, dag: DAG, start_date: Incomplete | None = ..., end_date: Incomplete | None = ..., mark_success: bool = ..., donot_pickle: bool = ..., ignore_first_depends_on_past: bool = ..., ignore_task_deps: bool = ..., pool: Incomplete | None = ..., delay_on_limit_secs: float = ..., verbose: bool = ..., conf: Incomplete | None = ..., rerun_failed_tasks: bool = ..., run_backwards: bool = ..., run_at_least_once: bool = ..., continue_on_failures: bool = ..., disable_retry: bool = ...) -> None: ...
    def reset_state_for_orphaned_tasks(self, *args, **kwargs) -> int | None: ...
