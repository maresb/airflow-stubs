from airflow import DAG as DAG
from airflow.api_connexion import security as security
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.schemas.task_schema import TaskCollection as TaskCollection, task_collection_schema as task_collection_schema, task_schema as task_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.exceptions import TaskNotFound as TaskNotFound
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app

def get_task(*, dag_id: str, task_id: str) -> APIResponse: ...
def get_tasks(*, dag_id: str, order_by: str = 'task_id') -> APIResponse: ...
