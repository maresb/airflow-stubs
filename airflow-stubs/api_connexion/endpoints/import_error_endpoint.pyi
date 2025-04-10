from airflow.api_connexion import security as security
from airflow.api_connexion.exceptions import NotFound as NotFound, PermissionDenied as PermissionDenied
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.error_schema import ImportErrorCollection as ImportErrorCollection, import_error_collection_schema as import_error_collection_schema, import_error_schema as import_error_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.batch_apis import IsAuthorizedDagRequest as IsAuthorizedDagRequest
from airflow.auth.managers.models.resource_details import AccessView as AccessView, DagDetails as DagDetails
from airflow.models.dag import DagModel as DagModel
from airflow.models.errors import ParseImportError as ParseImportError
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from sqlalchemy.orm import Session as Session

def get_import_error(*, import_error_id: int, session: Session = ...) -> APIResponse: ...
def get_import_errors(*, limit: int, offset: int | None = None, order_by: str = 'import_error_id', session: Session = ...) -> APIResponse: ...
