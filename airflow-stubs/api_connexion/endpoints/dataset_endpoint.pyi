from airflow.api_connexion import security as security
from airflow.api_connexion.endpoints.request_dict import get_json_request_dict as get_json_request_dict
from airflow.api_connexion.exceptions import BadRequest as BadRequest, NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_datetime as format_datetime, format_parameters as format_parameters
from airflow.api_connexion.schemas.dataset_schema import DagScheduleDatasetReference as DagScheduleDatasetReference, DatasetCollection as DatasetCollection, DatasetEventCollection as DatasetEventCollection, QueuedEvent as QueuedEvent, QueuedEventCollection as QueuedEventCollection, TaskOutletDatasetReference as TaskOutletDatasetReference, create_dataset_event_schema as create_dataset_event_schema, dataset_collection_schema as dataset_collection_schema, dataset_event_collection_schema as dataset_event_collection_schema, dataset_event_schema as dataset_event_schema, dataset_schema as dataset_schema, queued_event_collection_schema as queued_event_collection_schema, queued_event_schema as queued_event_schema
from airflow.api_connexion.types import APIResponse as APIResponse
from airflow.datasets import Dataset as Dataset
from airflow.datasets.manager import dataset_manager as dataset_manager
from airflow.models.dataset import DatasetDagRunQueue as DatasetDagRunQueue, DatasetEvent as DatasetEvent, DatasetModel as DatasetModel
from airflow.utils import timezone as timezone
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.www.decorators import action_logging as action_logging
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from sqlalchemy.orm import Session as Session

RESOURCE_EVENT_PREFIX: str

def get_dataset(*, uri: str, session: Session = ...) -> APIResponse: ...
def get_datasets(*, limit: int, offset: int = 0, uri_pattern: str | None = None, dag_ids: str | None = None, order_by: str = 'id', session: Session = ...) -> APIResponse: ...
def get_dataset_events(*, limit: int, offset: int = 0, order_by: str = 'timestamp', dataset_id: int | None = None, source_dag_id: str | None = None, source_task_id: str | None = None, source_run_id: str | None = None, source_map_index: int | None = None, session: Session = ...) -> APIResponse: ...
def get_dag_dataset_queued_event(*, dag_id: str, uri: str, before: str | None = None, session: Session = ...) -> APIResponse: ...
def delete_dag_dataset_queued_event(*, dag_id: str, uri: str, before: str | None = None, session: Session = ...) -> APIResponse: ...
def get_dag_dataset_queued_events(*, dag_id: str, before: str | None = None, session: Session = ...) -> APIResponse: ...
def delete_dag_dataset_queued_events(*, dag_id: str, before: str | None = None, session: Session = ...) -> APIResponse: ...
def get_dataset_queued_events(*, uri: str, before: str | None = None, session: Session = ...) -> APIResponse: ...
def delete_dataset_queued_events(*, uri: str, before: str | None = None, session: Session = ...) -> APIResponse: ...
def create_dataset_event(session: Session = ...) -> APIResponse: ...
