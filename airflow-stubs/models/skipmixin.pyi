from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.operator import Operator as Operator
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.models.taskmixin import DAGNode as DAGNode
from airflow.serialization.pydantic.dag_run import DagRunPydantic as DagRunPydantic
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.utils import timezone as timezone
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import tuple_in_condition as tuple_in_condition
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from pendulum import DateTime as DateTime
from sqlalchemy import Session as Session
from typing import Iterable

XCOM_SKIPMIXIN_KEY: str
XCOM_SKIPMIXIN_SKIPPED: str
XCOM_SKIPMIXIN_FOLLOWED: str

class SkipMixin(LoggingMixin):
    def skip(self, dag_run: DagRun | DagRunPydantic, execution_date: DateTime, tasks: Iterable[DAGNode], map_index: int = -1): ...
    @staticmethod
    def skip_all_except(ti: TaskInstance | TaskInstancePydantic, branch_task_ids: None | str | Iterable[str]): ...
