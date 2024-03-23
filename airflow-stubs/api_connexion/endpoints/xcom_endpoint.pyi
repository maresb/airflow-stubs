import airflow.api_connexion.security as security
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.xcom_schema import XComCollection as XComCollection, xcom_collection_schema as xcom_collection_schema, xcom_schema as xcom_schema
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.configuration import conf as conf
from airflow.models.dagrun import DR as DR
from airflow.models.xcom import XCom as XCom
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import provide_session as provide_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

TYPE_CHECKING: bool
NEW_SESSION: None
def get_xcom_entries(*args, **kwargs) -> APIResponse: ...
def get_xcom_entry(*args, **kwargs) -> APIResponse: ...
