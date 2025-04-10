import datetime
from _typeshed import Incomplete
from airflow.api.common.trigger_dag import trigger_dag as trigger_dag
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, AirflowSkipException as AirflowSkipException, DagNotFound as DagNotFound, DagRunAlreadyExists as DagRunAlreadyExists, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.baseoperatorlink import BaseOperatorLink as BaseOperatorLink
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.models.xcom import XCom as XCom
from airflow.triggers.external_task import DagStateTrigger as DagStateTrigger
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context
from airflow.utils.helpers import build_airflow_url_with_query as build_airflow_url_with_query
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState
from airflow.utils.types import DagRunType as DagRunType
from sqlalchemy.orm.session import Session as Session
from typing import Any, Sequence

XCOM_LOGICAL_DATE_ISO: str
XCOM_RUN_ID: str

class TriggerDagRunLink(BaseOperatorLink):
    name: str
    def get_link(self, operator: BaseOperator, *, ti_key: TaskInstanceKey) -> str: ...

class TriggerDagRunOperator(BaseOperator):
    template_fields: Sequence[str]
    template_fields_renderers: Incomplete
    ui_color: str
    operator_extra_links: Incomplete
    trigger_dag_id: Incomplete
    trigger_run_id: Incomplete
    conf: Incomplete
    reset_dag_run: Incomplete
    wait_for_completion: Incomplete
    poke_interval: Incomplete
    allowed_states: Incomplete
    failed_states: Incomplete
    skip_when_already_exists: Incomplete
    logical_date: Incomplete
    def __init__(self, *, trigger_dag_id: str, trigger_run_id: str | None = None, conf: dict | None = None, logical_date: str | datetime.datetime | None = None, reset_dag_run: bool = False, wait_for_completion: bool = False, poke_interval: int = 60, allowed_states: list[str | DagRunState] | None = None, failed_states: list[str | DagRunState] | None = None, skip_when_already_exists: bool = False, deferrable: bool = ..., execution_date: str | datetime.datetime | None = None, **kwargs) -> None: ...
    def execute(self, context: Context): ...
    def execute_complete(self, context: Context, session: Session, event: tuple[str, dict[str, Any]]): ...
