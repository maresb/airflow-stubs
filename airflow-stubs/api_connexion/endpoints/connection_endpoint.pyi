import airflow.api_connexion.security as security
import airflow.security.permissions as permissions
import airflow.utils.helpers as helpers
from airflow.api_connexion.endpoints.update_mask import extract_update_mask_data as extract_update_mask_data
from airflow.api_connexion.exceptions import AlreadyExists as AlreadyExists, BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.connection_schema import ConnectionCollection as ConnectionCollection, connection_collection_schema as connection_collection_schema, connection_schema as connection_schema, connection_test_schema as connection_test_schema
from airflow.configuration import conf as conf
from airflow.models.connection import Connection as Connection
from airflow.utils.log.action_logger import action_event_from_permission as action_event_from_permission
from airflow.utils.session import provide_session as provide_session
from airflow.utils.strings import get_random_string as get_random_string
from airflow.www.decorators import action_logging as action_logging

TYPE_CHECKING: bool
NoContent: object
CONN_ENV_PREFIX: str
NEW_SESSION: None
RESOURCE_EVENT_PREFIX: str
def delete_connection(*args, **kwargs) -> APIResponse: ...
def get_connection(*args, **kwargs) -> APIResponse: ...
def get_connections(*args, **kwargs) -> APIResponse: ...
def patch_connection(*args, **kwargs) -> APIResponse: ...
def post_connection(*args, **kwargs) -> APIResponse: ...
def test_connection(*args, **kwargs) -> APIResponse: ...
