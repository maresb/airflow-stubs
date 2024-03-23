import airflow.api_connexion.security as security
import airflow.security.permissions as permissions
from airflow.api_connexion.endpoints.request_dict import get_json_request_dict as get_json_request_dict
from airflow.api_connexion.endpoints.update_mask import extract_update_mask_data as extract_update_mask_data
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.variable_schema import variable_collection_schema as variable_collection_schema, variable_schema as variable_schema
from airflow.models.variable import Variable as Variable
from airflow.utils.log.action_logger import action_event_from_permission as action_event_from_permission
from airflow.utils.session import provide_session as provide_session
from airflow.www.decorators import action_logging as action_logging
from flask.wrappers import Response

TYPE_CHECKING: bool
NEW_SESSION: None
RESOURCE_EVENT_PREFIX: str
def delete_variable(*args, **kwargs) -> Response: ...
def get_variable(*args, **kwargs) -> Response: ...
def get_variables(*args, **kwargs) -> Response: ...
def patch_variable(*args, **kwargs) -> Response: ...
def post_variables(*args, **kwargs) -> Response: ...
