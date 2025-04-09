from airflow import DAG as DAG
from airflow.api_connexion import security as security
from airflow.api_connexion.exceptions import NotFound as NotFound
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.exceptions import TaskNotFound as TaskNotFound
from airflow.models.dagbag import DagBag as DagBag
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm.session import Session as Session

def get_extra_links(*, dag_id: str, dag_run_id: str, task_id: str, map_index: int = -1, session: Session = ...) -> APIResponse: ...
