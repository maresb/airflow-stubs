from airflow.api_connexion import security as security
from airflow.api_connexion.exceptions import NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.event_log_schema import EventLogCollection as EventLogCollection, event_log_collection_schema as event_log_collection_schema, event_log_schema as event_log_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.models import Log as Log
from airflow.utils import timezone as timezone
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm import Session as Session

def get_event_log(*, event_log_id: int, session: Session = ...) -> APIResponse: ...
def get_event_logs(*, dag_id: str | None = None, task_id: str | None = None, run_id: str | None = None, map_index: int | None = None, try_number: int | None = None, owner: str | None = None, event: str | None = None, excluded_events: str | None = None, included_events: str | None = None, before: str | None = None, after: str | None = None, limit: int, offset: int | None = None, order_by: str = 'event_log_id', session: Session = ...) -> APIResponse: ...
