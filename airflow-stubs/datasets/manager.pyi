from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.configuration import conf as conf
from airflow.datasets import Dataset as Dataset
from airflow.listeners.listener import get_listener_manager as get_listener_manager
from airflow.models.dag import DagModel as DagModel
from airflow.models.dagbag import DagPriorityParsingRequest as DagPriorityParsingRequest
from airflow.models.dataset import DagScheduleDatasetAliasReference as DagScheduleDatasetAliasReference, DagScheduleDatasetReference as DagScheduleDatasetReference, DatasetAliasModel as DatasetAliasModel, DatasetDagRunQueue as DatasetDagRunQueue, DatasetEvent as DatasetEvent, DatasetModel as DatasetModel
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.stats import Stats as Stats
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from collections.abc import Iterable
from sqlalchemy.orm.session import Session as Session

class DatasetManager(LoggingMixin):
    def __init__(self, **kwargs) -> None: ...
    def create_datasets(self, dataset_models: list[DatasetModel], session: Session) -> None: ...
    @classmethod
    def register_dataset_change(cls, *, task_instance: TaskInstance | None = None, dataset: Dataset, extra: Incomplete | None = None, session: Session = ..., source_alias_names: Iterable[str] | None = None, **kwargs) -> DatasetEvent | None: ...
    def notify_dataset_created(self, dataset: Dataset): ...
    @classmethod
    def notify_dataset_changed(cls, dataset: Dataset): ...

def resolve_dataset_manager() -> DatasetManager: ...

dataset_manager: Incomplete
