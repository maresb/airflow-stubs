import datetime
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, AirflowSkipException as AirflowSkipException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.baseoperatorlink import BaseOperatorLink as BaseOperatorLink
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.operators.empty import EmptyOperator as EmptyOperator
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.triggers.external_task import WorkflowTrigger as WorkflowTrigger
from airflow.utils.context import Context as Context
from airflow.utils.file import correct_maybe_zipped as correct_maybe_zipped
from airflow.utils.helpers import build_airflow_url_with_query as build_airflow_url_with_query
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import State as State, TaskInstanceState as TaskInstanceState
from sqlalchemy.orm import Session as Session
from typing import Callable, Collection, Iterable

class ExternalDagLink(BaseOperatorLink):
    name: str
    def get_link(self, operator: BaseOperator, *, ti_key: TaskInstanceKey) -> str: ...

class ExternalTaskSensor(BaseSensorOperator):
    template_fields: Incomplete
    ui_color: str
    operator_extra_links: Incomplete
    allowed_states: Incomplete
    skipped_states: Incomplete
    failed_states: Incomplete
    execution_delta: Incomplete
    execution_date_fn: Incomplete
    external_dag_id: Incomplete
    external_task_id: Incomplete
    external_task_ids: Incomplete
    external_task_group_id: Incomplete
    check_existence: Incomplete
    deferrable: Incomplete
    poll_interval: Incomplete
    def __init__(self, *, external_dag_id: str, external_task_id: str | None = None, external_task_ids: Collection[str] | None = None, external_task_group_id: str | None = None, allowed_states: Iterable[str] | None = None, skipped_states: Iterable[str] | None = None, failed_states: Iterable[str] | None = None, execution_delta: datetime.timedelta | None = None, execution_date_fn: Callable | None = None, check_existence: bool = False, poll_interval: float = 2.0, deferrable: bool = ..., **kwargs) -> None: ...
    def poke(self, context: Context, session: Session = ...) -> bool: ...
    def execute(self, context: Context) -> None: ...
    def execute_complete(self, context, event: Incomplete | None = None) -> None: ...
    def get_count(self, dttm_filter, session, states) -> int: ...
    def get_external_task_group_task_ids(self, session, dttm_filter): ...

class ExternalTaskMarker(EmptyOperator):
    template_fields: Incomplete
    ui_color: str
    operator_extra_links: Incomplete
    external_dag_id: Incomplete
    external_task_id: Incomplete
    execution_date: Incomplete
    recursion_depth: Incomplete
    def __init__(self, *, external_dag_id: str, external_task_id: str, execution_date: str | datetime.datetime | None = '{{ logical_date.isoformat() }}', recursion_depth: int = 10, **kwargs) -> None: ...
    @classmethod
    def get_serialized_fields(cls): ...

class ExternalTaskSensorLink(ExternalDagLink):
    def __attrs_post_init__(self) -> None: ...
    def __init__(self) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
