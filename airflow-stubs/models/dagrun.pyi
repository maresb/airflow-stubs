from _typeshed import Incomplete
from airflow import settings as settings
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.callbacks.callback_requests import DagCallbackRequest as DagCallbackRequest
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning, TaskNotFound as TaskNotFound
from airflow.listeners.listener import get_listener_manager as get_listener_manager
from airflow.models import Log as Log
from airflow.models.abstractoperator import NotMapped as NotMapped
from airflow.models.base import Base as Base, StringID as StringID
from airflow.models.dag import DAG as DAG
from airflow.models.expandinput import NotFullyPopulated as NotFullyPopulated
from airflow.models.operator import Operator as Operator
from airflow.models.taskinstance import TaskInstance as TI
from airflow.models.tasklog import LogTemplate as LogTemplate
from airflow.serialization.pydantic.dag_run import DagRunPydantic as DagRunPydantic
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.serialization.pydantic.tasklog import LogTemplatePydantic as LogTemplatePydantic
from airflow.stats import Stats as Stats
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.ti_deps.dependencies_states import SCHEDULEABLE_STATES as SCHEDULEABLE_STATES
from airflow.traces.tracer import Trace as Trace
from airflow.typing_compat import Literal as Literal
from airflow.utils import timezone as timezone
from airflow.utils.dates import datetime_to_nano as datetime_to_nano
from airflow.utils.helpers import chunks as chunks, is_container as is_container, prune_dict as prune_dict
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime, nulls_first as nulls_first, tuple_in_condition as tuple_in_condition, with_row_locks as with_row_locks
from airflow.utils.state import DagRunState as DagRunState, State as State, TaskInstanceState as TaskInstanceState
from airflow.utils.types import ArgNotSet as ArgNotSet, DagRunType as DagRunType, NOTSET as NOTSET
from datetime import datetime
from sqlalchemy.orm import Query as Query, Session as Session
from typing import Any, Iterable, Iterator, NamedTuple, TypeVar

CreatedTasks = TypeVar('CreatedTasks', Iterator['dict[str, Any]'], Iterator[TI])
RUN_ID_REGEX: str

class TISchedulingDecision(NamedTuple):
    tis: list[TI]
    schedulable_tis: list[TI]
    changed_tis: bool
    unfinished_tis: list[TI]
    finished_tis: list[TI]

class DagRun(Base, LoggingMixin):
    __tablename__: str
    id: Incomplete
    dag_id: Incomplete
    queued_at: Incomplete
    execution_date: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    run_id: Incomplete
    creating_job_id: Incomplete
    external_trigger: Incomplete
    run_type: Incomplete
    conf: Incomplete
    data_interval_start: Incomplete
    data_interval_end: Incomplete
    last_scheduling_decision: Incomplete
    dag_hash: Incomplete
    log_template_id: Incomplete
    updated_at: Incomplete
    clear_number: Incomplete
    dag: DAG | None
    __table_args__: Incomplete
    task_instances: Incomplete
    dag_model: Incomplete
    dag_run_note: Incomplete
    note: Incomplete
    DEFAULT_DAGRUNS_TO_EXAMINE: Incomplete
    def __init__(self, dag_id: str | None = None, run_id: str | None = None, queued_at: datetime | None | ArgNotSet = ..., execution_date: datetime | None = None, start_date: datetime | None = None, external_trigger: bool | None = None, conf: Any | None = None, state: DagRunState | None = None, run_type: str | None = None, dag_hash: str | None = None, creating_job_id: int | None = None, data_interval: tuple[datetime, datetime] | None = None) -> None: ...
    def validate_run_id(self, key: str, run_id: str) -> str | None: ...
    @property
    def stats_tags(self) -> dict[str, str]: ...
    @property
    def logical_date(self) -> datetime: ...
    def get_state(self): ...
    def set_state(self, state: DagRunState) -> None: ...
    def state(self): ...
    def refresh_from_db(self, session: Session = ...) -> None: ...
    @classmethod
    def active_runs_of_dags(cls, dag_ids: Iterable[str] | None = None, only_running: bool = False, session: Session = ...) -> dict[str, int]: ...
    @classmethod
    def next_dagruns_to_examine(cls, state: DagRunState, session: Session, max_number: int | None = None) -> Query: ...
    @classmethod
    def find(cls, dag_id: str | list[str] | None = None, run_id: Iterable[str] | None = None, execution_date: datetime | Iterable[datetime] | None = None, state: DagRunState | None = None, external_trigger: bool | None = None, no_backfills: bool = False, run_type: DagRunType | None = None, session: Session = ..., execution_start_date: datetime | None = None, execution_end_date: datetime | None = None) -> list[DagRun]: ...
    @classmethod
    def find_duplicate(cls, dag_id: str, run_id: str, execution_date: datetime, session: Session = ...) -> DagRun | None: ...
    @staticmethod
    def generate_run_id(run_type: DagRunType, execution_date: datetime) -> str: ...
    @staticmethod
    def fetch_task_instances(dag_id: str | None = None, run_id: str | None = None, task_ids: list[str] | None = None, state: Iterable[TaskInstanceState | None] | None = None, session: Session = ...) -> list[TI]: ...
    def get_task_instances(self, state: Iterable[TaskInstanceState | None] | None = None, session: Session = ...) -> list[TI]: ...
    def get_task_instance(self, task_id: str, session: Session = ..., *, map_index: int = -1) -> TI | TaskInstancePydantic | None: ...
    @staticmethod
    def fetch_task_instance(dag_id: str, dag_run_id: str, task_id: str, session: Session = ..., map_index: int = -1) -> TI | TaskInstancePydantic | None: ...
    def get_dag(self) -> DAG: ...
    @staticmethod
    def get_previous_dagrun(dag_run: DagRun | DagRunPydantic, state: DagRunState | None = None, session: Session = ...) -> DagRun | None: ...
    @staticmethod
    def get_previous_scheduled_dagrun(dag_run_id: int, session: Session = ...) -> DagRun | None: ...
    def update_state(self, session: Session = ..., execute_callbacks: bool = True) -> tuple[list[TI], DagCallbackRequest | None]: ...
    def task_instance_scheduling_decisions(self, session: Session = ...) -> TISchedulingDecision: ...
    def notify_dagrun_state_changed(self, msg: str = ''): ...
    def verify_integrity(self, *, session: Session = ...) -> None: ...
    @staticmethod
    def get_run(session: Session, dag_id: str, execution_date: datetime) -> DagRun | None: ...
    @property
    def is_backfill(self) -> bool: ...
    @classmethod
    def get_latest_runs(cls, session: Session = ...) -> list[DagRun]: ...
    def schedule_tis(self, schedulable_tis: Iterable[TI], session: Session = ..., max_tis_per_query: int | None = None) -> int: ...
    def get_log_template(self, *, session: Session = ...) -> LogTemplate | LogTemplatePydantic: ...
    def get_log_filename_template(self, *, session: Session = ...) -> str: ...

class DagRunNote(Base):
    __tablename__: str
    user_id: Incomplete
    dag_run_id: Incomplete
    content: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    dag_run: Incomplete
    __table_args__: Incomplete
    def __init__(self, content, user_id: Incomplete | None = None) -> None: ...
