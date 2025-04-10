from _typeshed import Incomplete
from airflow.api.common.experimental.get_task_instance import get_task_instance as get_task_instance
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning, TaskInstanceNotFound as TaskInstanceNotFound
from airflow.models import DagRun as DagRun
from airflow.models.dag import DAG as DAG, DagContext as DagContext
from airflow.models.pool import Pool as Pool
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.utils.context import Context as Context
from airflow.utils.session import NEW_SESSION as NEW_SESSION, create_session as create_session, provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState, TaskInstanceState as TaskInstanceState
from airflow.utils.types import DagRunType as DagRunType
from enum import Enum
from sqlalchemy.orm.session import Session as Session

class SkippedStatePropagationOptions(Enum):
    ALL_LEAVES = 'all_leaves'
    ANY_LEAF = 'any_leaf'

class SubDagOperator(BaseSensorOperator):
    ui_color: str
    ui_fgcolor: str
    subdag: DAG
    conf: Incomplete
    propagate_skipped_state: Incomplete
    def __init__(self, *, subdag: DAG, session: Session = ..., conf: dict | None = None, propagate_skipped_state: SkippedStatePropagationOptions | None = None, **kwargs) -> None: ...
    def pre_execute(self, context) -> None: ...
    def poke(self, context: Context): ...
    def post_execute(self, context, result: Incomplete | None = None) -> None: ...
