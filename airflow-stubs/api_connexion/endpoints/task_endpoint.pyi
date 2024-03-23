import airflow.api_connexion.security as security
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.schemas.task_schema import TaskCollection as TaskCollection, task_collection_schema as task_collection_schema, task_schema as task_schema
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.exceptions import TaskNotFound as TaskNotFound
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app

TYPE_CHECKING: bool
def get_task(*args, **kwargs) -> APIResponse: ...
def get_tasks(*args, **kwargs) -> APIResponse: ...
