from airflow.api_connexion import security as security
from airflow.api_connexion.schemas.dag_stats_schema import dag_stats_collection_schema as dag_stats_collection_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.models.dag import DagRun as DagRun
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from sqlalchemy.orm import Session as Session

def get_dag_stats(*, dag_ids: str, session: Session = ...) -> APIResponse: ...
