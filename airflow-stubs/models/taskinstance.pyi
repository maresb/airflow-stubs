import jinja2
import pendulum
from _typeshed import Incomplete
from airflow import settings as settings
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig, internal_api_call as internal_api_call
from airflow.compat.functools import cache as cache
from airflow.configuration import conf as conf
from airflow.datasets import Dataset as Dataset, DatasetAlias as DatasetAlias
from airflow.datasets.manager import dataset_manager as dataset_manager
from airflow.exceptions import AirflowException as AirflowException, AirflowFailException as AirflowFailException, AirflowRescheduleException as AirflowRescheduleException, AirflowSensorTimeout as AirflowSensorTimeout, AirflowSkipException as AirflowSkipException, AirflowTaskTerminated as AirflowTaskTerminated, AirflowTaskTimeout as AirflowTaskTimeout, DagRunNotFound as DagRunNotFound, RemovedInAirflow3Warning as RemovedInAirflow3Warning, TaskDeferralError as TaskDeferralError, TaskDeferred as TaskDeferred, UnmappableXComLengthPushed as UnmappableXComLengthPushed, UnmappableXComTypePushed as UnmappableXComTypePushed, XComForMappingNotPushed as XComForMappingNotPushed
from airflow.jobs.job import Job as Job
from airflow.listeners.listener import get_listener_manager as get_listener_manager
from airflow.models.abstractoperator import TaskStateChangeCallback as TaskStateChangeCallback
from airflow.models.base import Base as Base, StringID as StringID, TaskInstanceDependencies as TaskInstanceDependencies
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.dag import DAG as DAG, DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.dataset import DatasetAliasModel as DatasetAliasModel, DatasetEvent as DatasetEvent, DatasetModel as DatasetModel
from airflow.models.log import Log as Log
from airflow.models.operator import Operator as Operator
from airflow.models.param import process_params as process_params
from airflow.models.renderedtifields import get_serialized_template_fields as get_serialized_template_fields
from airflow.models.taskfail import TaskFail as TaskFail
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.models.taskmap import TaskMap as TaskMap
from airflow.models.taskreschedule import TaskReschedule as TaskReschedule
from airflow.models.xcom import LazyXComSelectSequence as LazyXComSelectSequence, XCom as XCom
from airflow.plugins_manager import integrate_macros_plugins as integrate_macros_plugins
from airflow.sentry import Sentry as Sentry
from airflow.serialization.pydantic.dag import DagModelPydantic as DagModelPydantic
from airflow.serialization.pydantic.dataset import DatasetEventPydantic as DatasetEventPydantic
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.settings import task_instance_mutation_hook as task_instance_mutation_hook
from airflow.stats import Stats as Stats
from airflow.templates import SandboxedEnvironment as SandboxedEnvironment
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.ti_deps.dependencies_deps import REQUEUEABLE_DEPS as REQUEUEABLE_DEPS, RUNNING_DEPS as RUNNING_DEPS
from airflow.timetables.base import DataInterval as DataInterval
from airflow.traces.tracer import Trace as Trace
from airflow.typing_compat import Literal as Literal, TypeGuard as TypeGuard
from airflow.utils import timezone as timezone
from airflow.utils.context import ConnectionAccessor as ConnectionAccessor, Context as Context, InletEventsAccessors as InletEventsAccessors, OutletEventAccessors as OutletEventAccessors, VariableAccessor as VariableAccessor, context_get_outlet_events as context_get_outlet_events, context_merge as context_merge
from airflow.utils.email import send_email as send_email
from airflow.utils.helpers import prune_dict as prune_dict, render_template_to_string as render_template_to_string
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.operator_helpers import ExecutionCallableRunner as ExecutionCallableRunner, context_to_airflow_vars as context_to_airflow_vars
from airflow.utils.platform import getuser as getuser
from airflow.utils.retries import run_with_db_retries as run_with_db_retries
from airflow.utils.session import NEW_SESSION as NEW_SESSION, create_session as create_session, provide_session as provide_session
from airflow.utils.sqlalchemy import ExecutorConfigType as ExecutorConfigType, ExtendedJSON as ExtendedJSON, UtcDateTime as UtcDateTime, tuple_in_condition as tuple_in_condition, with_row_locks as with_row_locks
from airflow.utils.state import DagRunState as DagRunState, JobState as JobState, State as State, TaskInstanceState as TaskInstanceState
from airflow.utils.task_group import MappedTaskGroup as MappedTaskGroup, TaskGroup as TaskGroup
from airflow.utils.task_instance_session import set_current_task_instance_session as set_current_task_instance_session
from airflow.utils.timeout import timeout as timeout
from airflow.utils.types import AttributeRemoved as AttributeRemoved
from airflow.utils.xcom import XCOM_RETURN_KEY as XCOM_RETURN_KEY
from datetime import datetime
from enum import Enum
from pathlib import PurePath
from sqlalchemy.orm.session import Session as Session
from sqlalchemy.sql.elements import BooleanClauseList as BooleanClauseList
from sqlalchemy.sql.expression import ColumnOperators as ColumnOperators
from types import TracebackType
from typing import Any, Callable, Collection, Generator, Iterable

TR = TaskReschedule
log: Incomplete
PAST_DEPENDS_MET: str

class TaskReturnCode(Enum):
    DEFERRED = 100

def set_current_context(context: Context) -> Generator[Context, None, None]: ...
def clear_task_instances(tis: list[TaskInstance], session: Session, activate_dag_runs: None = None, dag: DAG | None = None, dag_run_state: DagRunState | Literal[False] = ...) -> None: ...

class TaskInstance(Base, LoggingMixin):
    __tablename__: str
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    duration: Incomplete
    state: Incomplete
    try_number: Incomplete
    max_tries: Incomplete
    hostname: Incomplete
    unixname: Incomplete
    job_id: Incomplete
    pool: Incomplete
    pool_slots: Incomplete
    queue: Incomplete
    priority_weight: Incomplete
    operator: Incomplete
    custom_operator_name: Incomplete
    queued_dttm: Incomplete
    queued_by_job_id: Incomplete
    pid: Incomplete
    executor: Incomplete
    executor_config: Incomplete
    updated_at: Incomplete
    rendered_map_index: Incomplete
    external_executor_id: Incomplete
    trigger_id: Incomplete
    trigger_timeout: Incomplete
    next_method: Incomplete
    next_kwargs: Incomplete
    __table_args__: Incomplete
    dag_model: DagModel
    trigger: Incomplete
    triggerer_job: Incomplete
    dag_run: Incomplete
    rendered_task_instance_fields: Incomplete
    execution_date: Incomplete
    task_instance_note: Incomplete
    note: Incomplete
    task: Operator | None
    test_mode: bool
    is_trigger_log_context: bool
    run_as_user: str | None
    raw: bool | None
    def __init__(self, task: Operator, execution_date: datetime | None = None, run_id: str | None = None, state: str | None = None, map_index: int = -1) -> None: ...
    def __hash__(self): ...
    @property
    def stats_tags(self) -> dict[str, str]: ...
    @staticmethod
    def insert_mapping(run_id: str, task: Operator, map_index: int) -> dict[str, Any]: ...
    def init_on_load(self) -> None: ...
    @property
    def prev_attempted_tries(self) -> int: ...
    @property
    def next_try_number(self) -> int: ...
    @property
    def operator_name(self) -> str | None: ...
    def task_display_name(self) -> str: ...
    def command_as_list(self, mark_success: bool = False, ignore_all_deps: bool = False, ignore_task_deps: bool = False, ignore_depends_on_past: bool = False, wait_for_past_depends_before_skipping: bool = False, ignore_ti_state: bool = False, local: bool = False, pickle_id: int | None = None, raw: bool = False, job_id: str | None = None, pool: str | None = None, cfg_path: str | None = None) -> list[str]: ...
    @staticmethod
    def generate_command(dag_id: str, task_id: str, run_id: str, mark_success: bool = False, ignore_all_deps: bool = False, ignore_depends_on_past: bool = False, wait_for_past_depends_before_skipping: bool = False, ignore_task_deps: bool = False, ignore_ti_state: bool = False, local: bool = False, pickle_id: int | None = None, file_path: PurePath | str | None = None, raw: bool = False, job_id: str | None = None, pool: str | None = None, cfg_path: str | None = None, map_index: int = -1) -> list[str]: ...
    @property
    def log_url(self) -> str: ...
    @property
    def mark_success_url(self) -> str: ...
    def current_state(self, session: Session = ...) -> str: ...
    def error(self, session: Session = ...) -> None: ...
    @classmethod
    def get_task_instance(cls, dag_id: str, run_id: str, task_id: str, map_index: int, lock_for_update: bool = False, session: Session = ...) -> TaskInstance | TaskInstancePydantic | None: ...
    def refresh_from_db(self, session: Session = ..., lock_for_update: bool = False) -> None: ...
    def refresh_from_task(self, task: Operator, pool_override: str | None = None) -> None: ...
    def clear_xcom_data(self, session: Session = ...): ...
    @property
    def key(self) -> TaskInstanceKey: ...
    def set_state(self, state: str | None, session: Session = ...) -> bool: ...
    @property
    def is_premature(self) -> bool: ...
    def are_dependents_done(self, session: Session = ...) -> bool: ...
    def get_previous_dagrun(self, state: DagRunState | None = None, session: Session | None = None) -> DagRun | None: ...
    def get_previous_ti(self, state: DagRunState | None = None, session: Session = ...) -> TaskInstance | TaskInstancePydantic | None: ...
    @property
    def previous_ti(self) -> TaskInstance | TaskInstancePydantic | None: ...
    @property
    def previous_ti_success(self) -> TaskInstance | TaskInstancePydantic | None: ...
    def get_previous_execution_date(self, state: DagRunState | None = None, session: Session = ...) -> pendulum.DateTime | None: ...
    def get_previous_start_date(self, state: DagRunState | None = None, session: Session = ...) -> pendulum.DateTime | None: ...
    @property
    def previous_start_date_success(self) -> pendulum.DateTime | None: ...
    def are_dependencies_met(self, dep_context: DepContext | None = None, session: Session = ..., verbose: bool = False) -> bool: ...
    def get_failed_dep_statuses(self, dep_context: DepContext | None = None, session: Session = ...): ...
    def next_retry_datetime(self): ...
    def ready_for_retry(self) -> bool: ...
    def get_dagrun(self, session: Session = ...) -> DagRun: ...
    @classmethod
    def ensure_dag(cls, task_instance: TaskInstance | TaskInstancePydantic, session: Session = ...) -> DAG: ...
    def check_and_change_state_before_execution(self, verbose: bool = True, ignore_all_deps: bool = False, ignore_depends_on_past: bool = False, wait_for_past_depends_before_skipping: bool = False, ignore_task_deps: bool = False, ignore_ti_state: bool = False, mark_success: bool = False, test_mode: bool = False, job_id: str | None = None, pool: str | None = None, external_executor_id: str | None = None, session: Session = ...) -> bool: ...
    def emit_state_change_metric(self, new_state: TaskInstanceState) -> None: ...
    def clear_next_method_args(self) -> None: ...
    def defer_task(self, exception: TaskDeferred | None, session: Session = ...) -> None: ...
    def run(self, verbose: bool = True, ignore_all_deps: bool = False, ignore_depends_on_past: bool = False, wait_for_past_depends_before_skipping: bool = False, ignore_task_deps: bool = False, ignore_ti_state: bool = False, mark_success: bool = False, test_mode: bool = False, job_id: str | None = None, pool: str | None = None, session: Session = ..., raise_on_defer: bool = False) -> None: ...
    def dry_run(self) -> None: ...
    @staticmethod
    def get_truncated_error_traceback(error: BaseException, truncate_to: Callable) -> TracebackType | None: ...
    @classmethod
    def fetch_handle_failure_context(cls, ti: TaskInstance, error: None | str | BaseException, test_mode: bool | None = None, context: Context | None = None, force_fail: bool = False, *, session: Session, fail_stop: bool = False): ...
    @staticmethod
    def save_to_db(ti: TaskInstance | TaskInstancePydantic, session: Session = ..., refresh_dag: bool = True): ...
    def handle_failure(self, error: None | str | BaseException, test_mode: bool | None = None, context: Context | None = None, force_fail: bool = False, session: Session = ...) -> None: ...
    def is_eligible_to_retry(self): ...
    def get_template_context(self, session: Session | None = None, ignore_param_exceptions: bool = True) -> Context: ...
    def get_rendered_template_fields(self, session: Session = ...) -> None: ...
    def overwrite_params_with_dag_run_conf(self, params: dict, dag_run: DagRun): ...
    def render_templates(self, context: Context | None = None, jinja_env: jinja2.Environment | None = None) -> Operator: ...
    def render_k8s_pod_yaml(self) -> dict | None: ...
    def get_rendered_k8s_spec(self, session: Session = ...): ...
    def get_email_subject_content(self, exception: BaseException, task: BaseOperator | None = None) -> tuple[str, str, str]: ...
    def email_alert(self, exception, task: BaseOperator) -> None: ...
    def set_duration(self) -> None: ...
    def xcom_push(self, key: str, value: Any, execution_date: datetime | None = None, session: Session = ...) -> None: ...
    def xcom_pull(self, task_ids: str | Iterable[str] | None = None, dag_id: str | None = None, key: str = ..., include_prior_dates: bool = False, session: Session = ..., *, map_indexes: int | Iterable[int] | None = None, default: Any = None) -> Any: ...
    def get_num_running_task_instances(self, session: Session, same_dagrun: bool = False) -> int: ...
    def init_run_context(self, raw: bool = False) -> None: ...
    @staticmethod
    def filter_for_tis(tis: Iterable[TaskInstance | TaskInstanceKey]) -> BooleanClauseList | None: ...
    @classmethod
    def ti_selector_condition(cls, vals: Collection[str | tuple[str, int]]) -> ColumnOperators: ...
    def schedule_downstream_tasks(self, session: Session = ..., max_tis_per_query: int | None = None): ...
    def get_relevant_upstream_map_indexes(self, upstream: Operator, ti_count: int | None, *, session: Session) -> int | range | None: ...
    def clear_db_references(self, session: Session): ...
TaskInstanceStateType = tuple[TaskInstanceKey, TaskInstanceState]

class SimpleTaskInstance:
    dag_id: Incomplete
    task_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    try_number: Incomplete
    state: Incomplete
    executor: Incomplete
    executor_config: Incomplete
    run_as_user: Incomplete
    pool: Incomplete
    priority_weight: Incomplete
    queue: Incomplete
    key: Incomplete
    def __init__(self, dag_id: str, task_id: str, run_id: str, start_date: datetime | None, end_date: datetime | None, try_number: int, map_index: int, state: str, executor: str | None, executor_config: Any, pool: str, queue: str, key: TaskInstanceKey, run_as_user: str | None = None, priority_weight: int | None = None) -> None: ...
    def __eq__(self, other) -> bool: ...
    def as_dict(self): ...
    @classmethod
    def from_ti(cls, ti: TaskInstance) -> SimpleTaskInstance: ...
    @classmethod
    def from_dict(cls, obj_dict: dict) -> SimpleTaskInstance: ...

class TaskInstanceNote(TaskInstanceDependencies):
    __tablename__: str
    user_id: Incomplete
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    content: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    task_instance: Incomplete
    __table_args__: Incomplete
    def __init__(self, content, user_id: Incomplete | None = None) -> None: ...

STATICA_HACK: bool
