import airflow.api_connexion.security as security
import airflow.security.permissions as permissions
from airflow.api.common.mark_tasks import set_dag_run_state_to_failed as set_dag_run_state_to_failed, set_dag_run_state_to_queued as set_dag_run_state_to_queued, set_dag_run_state_to_success as set_dag_run_state_to_success
from airflow.api_connexion.endpoints.request_dict import get_json_request_dict as get_json_request_dict
from airflow.api_connexion.exceptions import AlreadyExists as AlreadyExists, BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_datetime as format_datetime, format_parameters as format_parameters
from airflow.api_connexion.schemas.dag_run_schema import DAGRunCollection as DAGRunCollection, clear_dagrun_form_schema as clear_dagrun_form_schema, dagrun_collection_schema as dagrun_collection_schema, dagrun_schema as dagrun_schema, dagruns_batch_form_schema as dagruns_batch_form_schema, set_dagrun_note_form_schema as set_dagrun_note_form_schema, set_dagrun_state_form_schema as set_dagrun_state_form_schema
from airflow.api_connexion.schemas.dataset_schema import DatasetEventCollection as DatasetEventCollection, dataset_event_collection_schema as dataset_event_collection_schema
from airflow.api_connexion.schemas.task_instance_schema import TaskInstanceReferenceCollection as TaskInstanceReferenceCollection, task_instance_reference_collection_schema as task_instance_reference_collection_schema
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagrun import DagRun as DagRun
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.log.action_logger import action_event_from_permission as action_event_from_permission
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState
from airflow.utils.types import DagRunType as DagRunType
from airflow.www.decorators import action_logging as action_logging
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

TYPE_CHECKING: bool
NoContent: object
NEW_SESSION: None
RESOURCE_EVENT_PREFIX: str
def delete_dag_run(*args, **kwargs) -> APIResponse: ...
def get_dag_run(*args, **kwargs) -> APIResponse: ...
def get_upstream_dataset_events(*args, **kwargs) -> APIResponse: ...
def get_dag_runs(*args, **kwargs): ...
def get_dag_runs_batch(*args, **kwargs) -> APIResponse: ...
def post_dag_run(*args, **kwargs) -> APIResponse: ...
def update_dag_run_state(*args, **kwargs) -> APIResponse: ...
def clear_dag_run(*args, **kwargs) -> APIResponse: ...
def set_dag_run_note(*args, **kwargs) -> APIResponse: ...
