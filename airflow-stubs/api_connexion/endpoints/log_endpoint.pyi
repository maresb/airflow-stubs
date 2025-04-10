from airflow.api_connexion import security as security
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.schemas.log_schema import LogResponseObject as LogResponseObject, logs_schema as logs_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.exceptions import TaskNotFound as TaskNotFound
from airflow.models import TaskInstance as TaskInstance, Trigger as Trigger
from airflow.models.taskinstancehistory import TaskInstanceHistory as TaskInstanceHistory
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.log.log_reader import TaskLogReader as TaskLogReader
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm import Session as Session

def get_log(*, dag_id: str, dag_run_id: str, task_id: str, task_try_number: int, full_content: bool = False, map_index: int = -1, token: str | None = None, session: Session = ...) -> APIResponse: ...
