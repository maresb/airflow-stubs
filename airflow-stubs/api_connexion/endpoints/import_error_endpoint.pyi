import airflow.api_connexion.security as security
from airflow.api_connexion.exceptions import NotFound as NotFound, PermissionDenied as PermissionDenied
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.error_schema import ImportErrorCollection as ImportErrorCollection, import_error_collection_schema as import_error_collection_schema, import_error_schema as import_error_schema
from airflow.auth.managers.models.resource_details import AccessView as AccessView, DagDetails as DagDetails
from airflow.models.dag import DagModel as DagModel
from airflow.models.errors import ImportErrorModel as ImportErrorModel
from airflow.utils.session import provide_session as provide_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

TYPE_CHECKING: bool
NEW_SESSION: None
def get_import_error(*args, **kwargs) -> APIResponse: ...
def get_import_errors(*args, **kwargs) -> APIResponse: ...
