from airflow.api_connexion import security as security
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.xcom_schema import XComCollection as XComCollection, xcom_collection_schema as xcom_collection_schema, xcom_schema_native as xcom_schema_native, xcom_schema_string as xcom_schema_string
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.models import XCom as XCom
from airflow.settings import conf as conf
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from sqlalchemy.orm import Session as Session

def get_xcom_entries(*, dag_id: str, dag_run_id: str, task_id: str, map_index: int | None = None, xcom_key: str | None = None, limit: int | None, offset: int | None = None, session: Session = ...) -> APIResponse: ...
def get_xcom_entry(*, dag_id: str, task_id: str, dag_run_id: str, xcom_key: str, map_index: int = -1, deserialize: bool = False, stringify: bool = True, session: Session = ...) -> APIResponse: ...
