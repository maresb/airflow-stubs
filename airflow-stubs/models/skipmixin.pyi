import airflow.utils.log.logging_mixin
import airflow.utils.timezone as timezone
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import create_session as create_session, provide_session as provide_session
from airflow.utils.sqlalchemy import tuple_in_condition as tuple_in_condition
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from typing import Iterable

TYPE_CHECKING: bool
NEW_SESSION: None
XCOM_SKIPMIXIN_KEY: str
XCOM_SKIPMIXIN_SKIPPED: str
XCOM_SKIPMIXIN_FOLLOWED: str

class SkipMixin(airflow.utils.log.logging_mixin.LoggingMixin):
    def skip(self, *args, **kwargs): ...
    def skip_all_except(self, ti: TaskInstance | TaskInstancePydantic, branch_task_ids: None | str | Iterable[str]): ...
