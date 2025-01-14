import airflow.models.baseoperator
import airflow.models.baseoperatorlink
import airflow.utils.timezone as timezone
from airflow.api.common.trigger_dag import trigger_dag as trigger_dag
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, DagNotFound as DagNotFound, DagRunAlreadyExists as DagRunAlreadyExists
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.baseoperatorlink import BaseOperatorLink as BaseOperatorLink
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.xcom import XCom as XCom
from airflow.triggers.external_task import DagStateTrigger as DagStateTrigger
from airflow.utils.helpers import build_airflow_url_with_query as build_airflow_url_with_query
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState
from airflow.utils.types import DagRunType as DagRunType
from typing import ClassVar

TYPE_CHECKING: bool
XCOM_EXECUTION_DATE_ISO: str
XCOM_RUN_ID: str

class TriggerDagRunLink(airflow.models.baseoperatorlink.BaseOperatorLink):
    name: ClassVar[str] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def get_link(self, operator: BaseOperator) -> str: ...

class TriggerDagRunOperator(airflow.models.baseoperator.BaseOperator):
    template_fields: ClassVar[tuple] = ...
    template_fields_renderers: ClassVar[dict] = ...
    ui_color: ClassVar[str] = ...
    operator_extra_links: ClassVar[list] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def execute(self, context: Context): ...
    def execute_complete(self, *args, **kwargs): ...
