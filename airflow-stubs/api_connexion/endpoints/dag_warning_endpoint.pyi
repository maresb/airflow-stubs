from airflow.api_connexion import security as security
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.dag_warning_schema import DagWarningCollection as DagWarningCollection, dag_warning_collection_schema as dag_warning_collection_schema
from airflow.api_connexion.security import get_readable_dags as get_readable_dags
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm import Session as Session

def get_dag_warnings(*, limit: int, dag_id: str | None = None, warning_type: str | None = None, offset: int | None = None, order_by: str = 'timestamp', session: Session = ...) -> APIResponse: ...
