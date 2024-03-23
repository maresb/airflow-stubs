import airflow.api_connexion.security as security
from airflow.api_connexion.exceptions import NotFound as NotFound
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.exceptions import TaskNotFound as TaskNotFound
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.session import provide_session as provide_session

TYPE_CHECKING: bool
NEW_SESSION: None
def get_extra_links(*args, **kwargs) -> APIResponse: ...
