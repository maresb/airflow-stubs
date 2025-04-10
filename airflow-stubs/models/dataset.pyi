from _typeshed import Incomplete
from airflow.datasets import Dataset as Dataset, DatasetAlias as DatasetAlias
from airflow.models.base import Base as Base, StringID as StringID
from airflow.settings import json as json
from airflow.utils import timezone as timezone
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

alias_association_table: Incomplete
dataset_alias_dataset_event_assocation_table: Incomplete

class DatasetAliasModel(Base):
    id: Incomplete
    name: Incomplete
    __tablename__: str
    __table_args__: Incomplete
    datasets: Incomplete
    dataset_events: Incomplete
    consuming_dags: Incomplete
    @classmethod
    def from_public(cls, obj: DatasetAlias) -> DatasetAliasModel: ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class DatasetModel(Base):
    id: Incomplete
    uri: Incomplete
    extra: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    is_orphaned: Incomplete
    consuming_dags: Incomplete
    producing_tasks: Incomplete
    __tablename__: str
    __table_args__: Incomplete
    @classmethod
    def from_public(cls, obj: Dataset) -> DatasetModel: ...
    def __init__(self, uri: str, **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class DagScheduleDatasetAliasReference(Base):
    alias_id: Incomplete
    dag_id: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    dataset_alias: Incomplete
    dag: Incomplete
    __tablename__: str
    __table_args__: Incomplete
    def __eq__(self, other): ...
    def __hash__(self): ...

class DagScheduleDatasetReference(Base):
    dataset_id: Incomplete
    dag_id: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    dataset: Incomplete
    dag: Incomplete
    queue_records: Incomplete
    __tablename__: str
    __table_args__: Incomplete
    def __eq__(self, other): ...
    def __hash__(self): ...

class TaskOutletDatasetReference(Base):
    dataset_id: Incomplete
    dag_id: Incomplete
    task_id: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    dataset: Incomplete
    __tablename__: str
    __table_args__: Incomplete
    def __eq__(self, other): ...
    def __hash__(self): ...

class DatasetDagRunQueue(Base):
    dataset_id: Incomplete
    target_dag_id: Incomplete
    created_at: Incomplete
    dataset: Incomplete
    __tablename__: str
    __table_args__: Incomplete
    def __eq__(self, other): ...
    def __hash__(self): ...

association_table: Incomplete

class DatasetEvent(Base):
    id: Incomplete
    dataset_id: Incomplete
    extra: Incomplete
    source_task_id: Incomplete
    source_dag_id: Incomplete
    source_run_id: Incomplete
    source_map_index: Incomplete
    timestamp: Incomplete
    __tablename__: str
    __table_args__: Incomplete
    created_dagruns: Incomplete
    source_aliases: Incomplete
    source_task_instance: Incomplete
    source_dag_run: Incomplete
    dataset: Incomplete
    @property
    def uri(self): ...
