from airflow.api_connexion import security as security
from airflow.api_connexion.endpoints.request_dict import get_json_request_dict as get_json_request_dict
from airflow.api_connexion.endpoints.update_mask import extract_update_mask_data as extract_update_mask_data
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.variable_schema import variable_collection_schema as variable_collection_schema, variable_schema as variable_schema
from airflow.api_connexion.types import UpdateMask as UpdateMask
from airflow.models import Variable as Variable
from airflow.security import permissions as permissions
from airflow.utils.log.action_logger import action_event_from_permission as action_event_from_permission
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.www.decorators import action_logging as action_logging
from flask import Response
from sqlalchemy.orm import Session as Session

RESOURCE_EVENT_PREFIX: str

def delete_variable(*, variable_key: str) -> Response: ...
def get_variable(*, variable_key: str, session: Session = ...) -> Response: ...
def get_variables(*, limit: int | None, order_by: str = 'id', offset: int | None = None, session: Session = ...) -> Response: ...
def patch_variable(*, variable_key: str, update_mask: UpdateMask = None, session: Session = ...) -> Response: ...
def post_variables() -> Response: ...
