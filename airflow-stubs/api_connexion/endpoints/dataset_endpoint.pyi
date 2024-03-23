import airflow.api_connexion.security as security
from airflow.api_connexion.exceptions import NotFound as NotFound
from airflow.api_connexion.parameters import apply_sorting as apply_sorting, check_limit as check_limit, format_parameters as format_parameters
from airflow.api_connexion.schemas.dataset_schema import DatasetCollection as DatasetCollection, DatasetEventCollection as DatasetEventCollection, dataset_collection_schema as dataset_collection_schema, dataset_event_collection_schema as dataset_event_collection_schema, dataset_schema as dataset_schema
from airflow.models.dataset import DatasetEvent as DatasetEvent, DatasetModel as DatasetModel
from airflow.utils.db import get_query_count as get_query_count
from airflow.utils.session import provide_session as provide_session

TYPE_CHECKING: bool
NEW_SESSION: None
def get_dataset(*args, **kwargs) -> APIResponse: ...
def get_datasets(*args, **kwargs) -> APIResponse: ...
def get_dataset_events(*args, **kwargs) -> APIResponse: ...
