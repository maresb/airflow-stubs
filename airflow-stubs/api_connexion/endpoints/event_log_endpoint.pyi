import airflow.api_connexion.security as security
import airflow.utils.timezone as timezone
from airflow.api_connexion.exceptions import NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.event_log_schema import EventLogCollection as EventLogCollection, event_log_collection_schema as event_log_collection_schema, event_log_schema as event_log_schema
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.models.log import Log as Log
from airflow.utils.session import provide_session as provide_session

TYPE_CHECKING: bool
NEW_SESSION: None
def get_event_log(*args, **kwargs) -> APIResponse: ...
def get_event_logs(*args, **kwargs) -> APIResponse: ...
