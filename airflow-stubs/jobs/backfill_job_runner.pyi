import attr
import pendulum
from _typeshed import Incomplete
from airflow import models as models
from airflow.exceptions import AirflowException as AirflowException, BackfillUnfinished as BackfillUnfinished, DagConcurrencyLimitReached as DagConcurrencyLimitReached, NoAvailablePoolSlot as NoAvailablePoolSlot, PoolNotFound as PoolNotFound, TaskConcurrencyLimitReached as TaskConcurrencyLimitReached, UnknownExecutorException as UnknownExecutorException
from airflow.executors.base_executor import BaseExecutor as BaseExecutor
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import Job as Job, perform_heartbeat as perform_heartbeat
from airflow.models import DAG as DAG, DagPickle as DagPickle
from airflow.models.abstractoperator import AbstractOperator as AbstractOperator
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.taskinstance import TaskInstance as TaskInstance, TaskInstanceKey as TaskInstanceKey
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.ti_deps.dependencies_deps import BACKFILL_QUEUED_DEPS as BACKFILL_QUEUED_DEPS
from airflow.timetables.base import DagRunInfo as DagRunInfo
from airflow.utils import helpers as helpers, timezone as timezone
from airflow.utils.configuration import tmp_configuration_copy as tmp_configuration_copy
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState, State as State, TaskInstanceState as TaskInstanceState
from airflow.utils.types import DagRunType as DagRunType
from sqlalchemy.orm.session import Session as Session

class BackfillJobRunner(BaseJobRunner, LoggingMixin):
    job_type: str
    STATES_COUNT_AS_RUNNING: Incomplete
    @attr.define
    class _DagRunTaskStatus:
        to_run: dict[TaskInstanceKey, TaskInstance] = ...
        running: dict[TaskInstanceKey, TaskInstance] = ...
        skipped: set[TaskInstanceKey] = ...
        succeeded: set[TaskInstanceKey] = ...
        failed: set[TaskInstanceKey] = ...
        not_ready: set[TaskInstanceKey] = ...
        deadlocked: set[TaskInstance] = ...
        active_runs: set[DagRun] = ...
        executed_dag_run_dates: set[pendulum.DateTime] = ...
        finished_runs: int = ...
        total_runs: int = ...
    dag: Incomplete
    dag_id: Incomplete
    bf_start_date: Incomplete
    bf_end_date: Incomplete
    mark_success: Incomplete
    donot_pickle: Incomplete
    ignore_first_depends_on_past: Incomplete
    ignore_task_deps: Incomplete
    pool: Incomplete
    delay_on_limit_secs: Incomplete
    verbose: Incomplete
    conf: Incomplete
    rerun_failed_tasks: Incomplete
    run_backwards: Incomplete
    run_at_least_once: Incomplete
    continue_on_failures: Incomplete
    disable_retry: Incomplete
    def __init__(self, job: Job, dag: DAG, start_date: Incomplete | None = None, end_date: Incomplete | None = None, mark_success: bool = False, donot_pickle: bool = False, ignore_first_depends_on_past: bool = False, ignore_task_deps: bool = False, pool: Incomplete | None = None, delay_on_limit_secs: float = 1.0, verbose: bool = False, conf: Incomplete | None = None, rerun_failed_tasks: bool = False, run_backwards: bool = False, run_at_least_once: bool = False, continue_on_failures: bool = False, disable_retry: bool = False) -> None: ...
    def reset_state_for_orphaned_tasks(self, filter_by_dag_run: DagRun | None = None, session: Session = ...) -> int | None: ...
