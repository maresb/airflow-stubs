import abc
import collections.abc
import jinja2
import pendulum
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, FailStopDagInvalidTriggerRule as FailStopDagInvalidTriggerRule, RemovedInAirflow3Warning as RemovedInAirflow3Warning, TaskDeferralError as TaskDeferralError, TaskDeferred as TaskDeferred
from airflow.lineage import apply_lineage as apply_lineage, prepare_lineage as prepare_lineage
from airflow.models.abstractoperator import AbstractOperator as AbstractOperator, DEFAULT_EXECUTOR as DEFAULT_EXECUTOR, DEFAULT_IGNORE_FIRST_DEPENDS_ON_PAST as DEFAULT_IGNORE_FIRST_DEPENDS_ON_PAST, DEFAULT_OWNER as DEFAULT_OWNER, DEFAULT_POOL_SLOTS as DEFAULT_POOL_SLOTS, DEFAULT_PRIORITY_WEIGHT as DEFAULT_PRIORITY_WEIGHT, DEFAULT_QUEUE as DEFAULT_QUEUE, DEFAULT_RETRIES as DEFAULT_RETRIES, DEFAULT_RETRY_DELAY as DEFAULT_RETRY_DELAY, DEFAULT_TASK_EXECUTION_TIMEOUT as DEFAULT_TASK_EXECUTION_TIMEOUT, DEFAULT_TRIGGER_RULE as DEFAULT_TRIGGER_RULE, DEFAULT_WAIT_FOR_PAST_DEPENDS_BEFORE_SKIPPING as DEFAULT_WAIT_FOR_PAST_DEPENDS_BEFORE_SKIPPING, DEFAULT_WEIGHT_RULE as DEFAULT_WEIGHT_RULE, TaskStateChangeCallback as TaskStateChangeCallback
from airflow.models.baseoperatorlink import BaseOperatorLink as BaseOperatorLink
from airflow.models.dag import DAG as DAG
from airflow.models.mappedoperator import OperatorPartial as OperatorPartial, validate_mapping_kwargs as validate_mapping_kwargs
from airflow.models.operator import Operator as Operator
from airflow.models.param import ParamsDict as ParamsDict
from airflow.models.pool import Pool as Pool
from airflow.models.taskinstance import TaskInstance as TaskInstance, clear_task_instances as clear_task_instances
from airflow.models.taskmixin import DependencyMixin as DependencyMixin
from airflow.models.xcom_arg import XComArg as XComArg
from airflow.serialization.enums import DagAttributeTypes as DagAttributeTypes
from airflow.task.priority_strategy import PriorityWeightStrategy as PriorityWeightStrategy, validate_and_load_priority_weight_strategy as validate_and_load_priority_weight_strategy
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.ti_deps.deps.mapped_task_upstream_dep import MappedTaskUpstreamDep as MappedTaskUpstreamDep
from airflow.ti_deps.deps.not_in_retry_period_dep import NotInRetryPeriodDep as NotInRetryPeriodDep
from airflow.ti_deps.deps.not_previously_skipped_dep import NotPreviouslySkippedDep as NotPreviouslySkippedDep
from airflow.ti_deps.deps.prev_dagrun_dep import PrevDagrunDep as PrevDagrunDep
from airflow.ti_deps.deps.trigger_rule_dep import TriggerRuleDep as TriggerRuleDep
from airflow.triggers.base import BaseTrigger as BaseTrigger, StartTriggerArgs as StartTriggerArgs
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context, context_get_outlet_events as context_get_outlet_events
from airflow.utils.decorators import fixup_decorator_warning_stack as fixup_decorator_warning_stack
from airflow.utils.edgemodifier import EdgeModifier as EdgeModifier
from airflow.utils.helpers import validate_instance_args as validate_instance_args, validate_key as validate_key
from airflow.utils.operator_helpers import ExecutionCallableRunner as ExecutionCallableRunner
from airflow.utils.operator_resources import Resources as Resources
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.setup_teardown import SetupTeardownContext as SetupTeardownContext
from airflow.utils.task_group import TaskGroup as TaskGroup
from airflow.utils.trigger_rule import TriggerRule as TriggerRule
from airflow.utils.types import ArgNotSet as ArgNotSet, AttributeRemoved as AttributeRemoved, NOTSET as NOTSET
from airflow.utils.xcom import XCOM_RETURN_KEY as XCOM_RETURN_KEY
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from sqlalchemy.orm import Session as Session
from types import ClassMethodDescriptorType, FunctionType
from typing import Any, Callable, Collection, Iterable, NoReturn, Sequence, TypeVar

ScheduleInterval = str | timedelta | relativedelta
TaskPreExecuteHook = Callable[[Context], None]
TaskPostExecuteHook = Callable[[Context, Any], None]
T = TypeVar('T', bound=FunctionType)
logger: Incomplete

def parse_retries(retries: Any) -> int | None: ...
def coerce_timedelta(value: float | timedelta, *, key: str) -> timedelta: ...
def coerce_resources(resources: dict[str, Any] | None) -> Resources | None: ...
def get_merged_defaults(dag: DAG | None, task_group: TaskGroup | None, task_params: collections.abc.MutableMapping | None, task_default_args: dict | None) -> tuple[dict, ParamsDict]: ...

class _PartialDescriptor:
    class_method: ClassMethodDescriptorType | None
    def __get__(self, obj: BaseOperator, cls: type[BaseOperator] | None = None) -> Callable[..., OperatorPartial]: ...

def partial(operator_class: type[BaseOperator], *, task_id: str, dag: DAG | None = None, task_group: TaskGroup | None = None, start_date: datetime | ArgNotSet = ..., end_date: datetime | ArgNotSet = ..., owner: str | ArgNotSet = ..., email: None | str | Iterable[str] | ArgNotSet = ..., params: collections.abc.MutableMapping | None = None, resources: dict[str, Any] | None | ArgNotSet = ..., trigger_rule: str | ArgNotSet = ..., depends_on_past: bool | ArgNotSet = ..., ignore_first_depends_on_past: bool | ArgNotSet = ..., wait_for_past_depends_before_skipping: bool | ArgNotSet = ..., wait_for_downstream: bool | ArgNotSet = ..., retries: int | None | ArgNotSet = ..., queue: str | ArgNotSet = ..., pool: str | ArgNotSet = ..., pool_slots: int | ArgNotSet = ..., execution_timeout: timedelta | None | ArgNotSet = ..., max_retry_delay: None | timedelta | float | ArgNotSet = ..., retry_delay: timedelta | float | ArgNotSet = ..., retry_exponential_backoff: bool | ArgNotSet = ..., priority_weight: int | ArgNotSet = ..., weight_rule: str | PriorityWeightStrategy | ArgNotSet = ..., sla: timedelta | None | ArgNotSet = ..., map_index_template: str | None | ArgNotSet = ..., max_active_tis_per_dag: int | None | ArgNotSet = ..., max_active_tis_per_dagrun: int | None | ArgNotSet = ..., on_execute_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] | ArgNotSet = ..., on_failure_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] | ArgNotSet = ..., on_success_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] | ArgNotSet = ..., on_retry_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] | ArgNotSet = ..., on_skipped_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] | ArgNotSet = ..., run_as_user: str | None | ArgNotSet = ..., executor: str | None | ArgNotSet = ..., executor_config: dict | None | ArgNotSet = ..., inlets: Any | None | ArgNotSet = ..., outlets: Any | None | ArgNotSet = ..., doc: str | None | ArgNotSet = ..., doc_md: str | None | ArgNotSet = ..., doc_json: str | None | ArgNotSet = ..., doc_yaml: str | None | ArgNotSet = ..., doc_rst: str | None | ArgNotSet = ..., task_display_name: str | None | ArgNotSet = ..., logger_name: str | None | ArgNotSet = ..., allow_nested_operators: bool = True, **kwargs) -> OperatorPartial: ...

class ExecutorSafeguard:
    test_mode: Incomplete
    @classmethod
    def decorator(cls, func): ...

class BaseOperatorMeta(abc.ABCMeta):
    def __new__(cls, name, bases, namespace, **kwargs): ...

BASEOPERATOR_ARGS_EXPECTED_TYPES: Incomplete

class BaseOperator(AbstractOperator, metaclass=BaseOperatorMeta):
    template_fields: Sequence[str]
    template_ext: Sequence[str]
    template_fields_renderers: dict[str, str]
    ui_color: str
    ui_fgcolor: str
    pool: str
    shallow_copy_attrs: Sequence[str]
    operator_extra_links: Collection[BaseOperatorLink]
    partial: Callable[..., OperatorPartial]
    supports_lineage: bool
    task_group: TaskGroup | None
    subdag: DAG | None
    start_date: pendulum.DateTime | None
    end_date: pendulum.DateTime | None
    start_trigger_args: StartTriggerArgs | None
    start_from_trigger: bool
    task_id: Incomplete
    owner: Incomplete
    email: Incomplete
    email_on_retry: Incomplete
    email_on_failure: Incomplete
    execution_timeout: Incomplete
    on_execute_callback: Incomplete
    on_failure_callback: Incomplete
    on_success_callback: Incomplete
    on_retry_callback: Incomplete
    on_skipped_callback: Incomplete
    executor: Incomplete
    executor_config: Incomplete
    run_as_user: Incomplete
    retries: Incomplete
    queue: Incomplete
    pool_slots: Incomplete
    sla: Incomplete
    trigger_rule: TriggerRule
    depends_on_past: bool
    ignore_first_depends_on_past: bool
    wait_for_past_depends_before_skipping: bool
    wait_for_downstream: bool
    retry_delay: Incomplete
    retry_exponential_backoff: Incomplete
    max_retry_delay: Incomplete
    params: ParamsDict | dict
    priority_weight: Incomplete
    weight_rule: Incomplete
    resources: Incomplete
    max_active_tis_per_dag: int | None
    max_active_tis_per_dagrun: int | None
    do_xcom_push: bool
    map_index_template: str | None
    multiple_outputs: bool
    doc_md: Incomplete
    doc_json: Incomplete
    doc_yaml: Incomplete
    doc_rst: Incomplete
    doc: Incomplete
    upstream_task_ids: set[str]
    downstream_task_ids: set[str]
    allow_nested_operators: bool
    inlets: list
    outlets: list
    def __init__(self, task_id: str, owner: str = ..., email: str | Iterable[str] | None = None, email_on_retry: bool = ..., email_on_failure: bool = ..., retries: int | None = ..., retry_delay: timedelta | float = ..., retry_exponential_backoff: bool = False, max_retry_delay: timedelta | float | None = None, start_date: datetime | None = None, end_date: datetime | None = None, depends_on_past: bool = False, ignore_first_depends_on_past: bool = ..., wait_for_past_depends_before_skipping: bool = ..., wait_for_downstream: bool = False, dag: DAG | None = None, params: collections.abc.MutableMapping | None = None, default_args: dict | None = None, priority_weight: int = ..., weight_rule: str | PriorityWeightStrategy = ..., queue: str = ..., pool: str | None = None, pool_slots: int = ..., sla: timedelta | None = None, execution_timeout: timedelta | None = ..., on_execute_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] = None, on_failure_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] = None, on_success_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] = None, on_retry_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] = None, on_skipped_callback: None | TaskStateChangeCallback | list[TaskStateChangeCallback] = None, pre_execute: TaskPreExecuteHook | None = None, post_execute: TaskPostExecuteHook | None = None, trigger_rule: str = ..., resources: dict[str, Any] | None = None, run_as_user: str | None = None, task_concurrency: int | None = None, map_index_template: str | None = None, max_active_tis_per_dag: int | None = None, max_active_tis_per_dagrun: int | None = None, executor: str | None = None, executor_config: dict | None = None, do_xcom_push: bool = True, multiple_outputs: bool = False, inlets: Any | None = None, outlets: Any | None = None, task_group: TaskGroup | None = None, doc: str | None = None, doc_md: str | None = None, doc_json: str | None = None, doc_yaml: str | None = None, doc_rst: str | None = None, task_display_name: str | None = None, logger_name: str | None = None, allow_nested_operators: bool = True, **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def __or__(self, other): ...
    def __gt__(self, other): ...
    def __lt__(self, other): ...
    def __setattr__(self, key, value) -> None: ...
    def add_inlets(self, inlets: Iterable[Any]): ...
    def add_outlets(self, outlets: Iterable[Any]): ...
    def get_inlet_defs(self): ...
    def get_outlet_defs(self): ...
    def get_dag(self) -> DAG | None: ...
    @property
    def dag(self) -> DAG: ...
    @dag.setter
    def dag(self, dag: DAG | None): ...
    @property
    def task_display_name(self) -> str: ...
    def has_dag(self): ...
    deps: frozenset[BaseTIDep]
    def prepare_for_execution(self) -> BaseOperator: ...
    def set_xcomargs_dependencies(self) -> None: ...
    def pre_execute(self, context: Any): ...
    def execute(self, context: Context) -> Any: ...
    def post_execute(self, context: Any, result: Any = None): ...
    def on_kill(self) -> None: ...
    def __deepcopy__(self, memo): ...
    def render_template_fields(self, context: Context, jinja_env: jinja2.Environment | None = None) -> None: ...
    def clear(self, start_date: datetime | None = None, end_date: datetime | None = None, upstream: bool = False, downstream: bool = False, session: Session = ...): ...
    def get_task_instances(self, start_date: datetime | None = None, end_date: datetime | None = None, session: Session = ...) -> list[TaskInstance]: ...
    def run(self, start_date: datetime | None = None, end_date: datetime | None = None, ignore_first_depends_on_past: bool = True, wait_for_past_depends_before_skipping: bool = False, ignore_ti_state: bool = False, mark_success: bool = False, test_mode: bool = False, session: Session = ...) -> None: ...
    def dry_run(self) -> None: ...
    def get_direct_relatives(self, upstream: bool = False) -> Iterable[Operator]: ...
    @property
    def operator_class(self) -> type[BaseOperator]: ...
    @property
    def task_type(self) -> str: ...
    @property
    def operator_name(self) -> str: ...
    @property
    def roots(self) -> list[BaseOperator]: ...
    @property
    def leaves(self) -> list[BaseOperator]: ...
    @property
    def output(self) -> XComArg: ...
    @property
    def is_setup(self) -> bool: ...
    @is_setup.setter
    def is_setup(self, value: bool) -> None: ...
    @property
    def is_teardown(self) -> bool: ...
    @is_teardown.setter
    def is_teardown(self, value: bool) -> None: ...
    @staticmethod
    def xcom_push(context: Any, key: str, value: Any, execution_date: datetime | None = None) -> None: ...
    @staticmethod
    def xcom_pull(context: Any, task_ids: str | list[str] | None = None, dag_id: str | None = None, key: str = ..., include_prior_dates: bool | None = None, session: Session = ...) -> Any: ...
    @classmethod
    def get_serialized_fields(cls): ...
    def serialize_for_task_group(self) -> tuple[DagAttributeTypes, Any]: ...
    @property
    def inherits_from_empty_operator(self): ...
    def defer(self, *, trigger: BaseTrigger, method_name: str, kwargs: dict[str, Any] | None = None, timeout: timedelta | None = None) -> NoReturn: ...
    def resume_execution(self, next_method: str, next_kwargs: dict[str, Any] | None, context: Context): ...
    def unmap(self, resolve: None | dict[str, Any] | tuple[Context, Session]) -> BaseOperator: ...
    def expand_start_from_trigger(self, *, context: Context, session: Session) -> bool: ...
    def expand_start_trigger_args(self, *, context: Context, session: Session) -> StartTriggerArgs | None: ...
Chainable = DependencyMixin | Sequence[DependencyMixin]

def chain(*tasks: DependencyMixin | Sequence[DependencyMixin]) -> None: ...
def cross_downstream(from_tasks: Sequence[DependencyMixin], to_tasks: DependencyMixin | Sequence[DependencyMixin]): ...
def chain_linear(*elements: DependencyMixin | Sequence[DependencyMixin]): ...
def __getattr__(name): ...
