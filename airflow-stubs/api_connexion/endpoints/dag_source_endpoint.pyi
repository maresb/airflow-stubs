import airflow.api_connexion.security as security
from airflow.api_connexion.exceptions import NotFound as NotFound, PermissionDenied as PermissionDenied
from airflow.api_connexion.schemas.dag_source_schema import dag_source_schema as dag_source_schema
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity, DagDetails as DagDetails
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagcode import DagCode as DagCode
from airflow.utils.session import provide_session as provide_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from flask.wrappers import Response

TYPE_CHECKING: bool
NEW_SESSION: None
def get_dag_source(*args, **kwargs) -> Response: ...
