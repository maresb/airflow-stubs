from airflow.api_connexion import security as security
from airflow.api_connexion.endpoints.update_mask import extract_update_mask_data as extract_update_mask_data
from airflow.api_connexion.exceptions import AlreadyExists as AlreadyExists, BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.connection_schema import ConnectionCollection as ConnectionCollection, connection_collection_schema as connection_collection_schema, connection_schema as connection_schema, connection_test_schema as connection_test_schema
from airflow.api_connexion.types import APIResponse as APIResponse, UpdateMask as UpdateMask
from airflow.configuration import conf as conf
from airflow.models import Connection as Connection
from airflow.secrets.environment_variables import CONN_ENV_PREFIX as CONN_ENV_PREFIX
from airflow.security import permissions as permissions
from airflow.utils import helpers as helpers
from airflow.utils.log.action_logger import action_event_from_permission as action_event_from_permission
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.strings import get_random_string as get_random_string
from airflow.www.decorators import action_logging as action_logging
from sqlalchemy.orm import Session as Session

RESOURCE_EVENT_PREFIX: str

def delete_connection(*, connection_id: str, session: Session = ...) -> APIResponse: ...
def get_connection(*, connection_id: str, session: Session = ...) -> APIResponse: ...
def get_connections(*, limit: int, offset: int = 0, order_by: str = 'id', session: Session = ...) -> APIResponse: ...
def patch_connection(*, connection_id: str, update_mask: UpdateMask = None, session: Session = ...) -> APIResponse: ...
def post_connection(*, session: Session = ...) -> APIResponse: ...
def test_connection() -> APIResponse: ...
