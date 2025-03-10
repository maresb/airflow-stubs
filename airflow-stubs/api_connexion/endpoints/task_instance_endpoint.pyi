import airflow.api_connexion.security as security
import typing
from airflow.api_connexion.endpoints.request_dict import get_json_request_dict as get_json_request_dict
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound, PermissionDenied as PermissionDenied
from airflow.api_connexion.parameters import format_datetime as format_datetime, format_parameters as format_parameters
from airflow.api_connexion.schemas.task_instance_schema import TaskInstanceCollection as TaskInstanceCollection, TaskInstanceReferenceCollection as TaskInstanceReferenceCollection, clear_task_instance_form as clear_task_instance_form, set_single_task_instance_state_form as set_single_task_instance_state_form, set_task_instance_note_form_schema as set_task_instance_note_form_schema, set_task_instance_state_form as set_task_instance_state_form, task_instance_batch_form as task_instance_batch_form, task_instance_collection_schema as task_instance_collection_schema, task_instance_reference_collection_schema as task_instance_reference_collection_schema, task_instance_reference_schema as task_instance_reference_schema, task_instance_schema as task_instance_schema
from airflow.api_connexion.security import get_readable_dags as get_readable_dags
from airflow.auth.managers.models.resource_details import DagAccessEntity as DagAccessEntity, DagDetails as DagDetails
from airflow.exceptions import TaskNotFound as TaskNotFound
from airflow.models.dagrun import DR as DR
from airflow.models.operator import needs_expansion as needs_expansion
from airflow.models.slamiss import SlaMiss as SlaMiss
from airflow.models.taskinstance import TI as TI, clear_task_instances as clear_task_instances
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState, TaskInstanceState as TaskInstanceState
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager

TYPE_CHECKING: bool
NEW_SESSION: None
T: typing.TypeVar
def get_task_instance(*args, **kwargs) -> APIResponse: ...
def get_mapped_task_instance(*args, **kwargs) -> APIResponse: ...
def get_mapped_task_instances(*args, **kwargs) -> APIResponse: ...
def get_task_instances(*args, **kwargs) -> APIResponse: ...
def get_task_instances_batch(*args, **kwargs) -> APIResponse: ...
def post_clear_task_instances(*args, **kwargs) -> APIResponse: ...
def post_set_task_instances_state(*args, **kwargs) -> APIResponse: ...
def set_mapped_task_instance_note() -> APIResponse: ...
def patch_task_instance(*args, **kwargs) -> APIResponse: ...
def patch_mapped_task_instance(*args, **kwargs) -> APIResponse: ...
def set_task_instance_note(*args, **kwargs) -> APIResponse: ...
