import airflow.api_connexion.security as security
from airflow.api_connexion.exceptions import AlreadyExists as AlreadyExists, BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.dag_schema import DAGCollection as DAGCollection, dag_detail_schema as dag_detail_schema, dag_schema as dag_schema, dags_collection_schema as dags_collection_schema
from airflow.exceptions import AirflowException as AirflowException, DagNotFound as DagNotFound
from airflow.models.dag import DagModel as DagModel, DagTag as DagTag
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import provide_session as provide_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

TYPE_CHECKING: bool
NoContent: object
NEW_SESSION: None
def get_dag(*args, **kwargs) -> APIResponse: ...
def get_dag_details(*args, **kwargs) -> APIResponse: ...
def get_dags(*args, **kwargs) -> APIResponse: ...
def patch_dag(*args, **kwargs) -> APIResponse: ...
def patch_dags(*args, **kwargs): ...
def delete_dag(*args, **kwargs) -> APIResponse: ...
