from _typeshed import Incomplete
from airflow.api_connexion.schemas.common_schema import JsonObjectField as JsonObjectField
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.dataset import DagScheduleDatasetReference as DagScheduleDatasetReference, DatasetAliasModel as DatasetAliasModel, DatasetEvent as DatasetEvent, DatasetModel as DatasetModel, TaskOutletDatasetReference as TaskOutletDatasetReference
from datetime import datetime
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class TaskOutletDatasetReferenceSchema(SQLAlchemySchema):
    class Meta:
        model = TaskOutletDatasetReference
    dag_id: Incomplete
    task_id: Incomplete
    created_at: Incomplete
    updated_at: Incomplete

class DagScheduleDatasetReferenceSchema(SQLAlchemySchema):
    class Meta:
        model = DagScheduleDatasetReference
    dag_id: Incomplete
    created_at: Incomplete
    updated_at: Incomplete

class DatasetAliasSchema(SQLAlchemySchema):
    class Meta:
        model = DatasetAliasModel
    id: Incomplete
    name: Incomplete

class DatasetSchema(SQLAlchemySchema):
    class Meta:
        model = DatasetModel
    id: Incomplete
    uri: Incomplete
    extra: Incomplete
    created_at: Incomplete
    updated_at: Incomplete
    producing_tasks: Incomplete
    consuming_dags: Incomplete
    aliases: Incomplete

class DatasetCollection(NamedTuple):
    datasets: list[DatasetModel]
    total_entries: int

class DatasetCollectionSchema(Schema):
    datasets: Incomplete
    total_entries: Incomplete

dataset_schema: Incomplete
dataset_collection_schema: Incomplete

class BasicDAGRunSchema(SQLAlchemySchema):
    class Meta:
        model = DagRun
        dateformat: str
    run_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    state: Incomplete
    data_interval_start: Incomplete
    data_interval_end: Incomplete

class DatasetEventSchema(SQLAlchemySchema):
    class Meta:
        model = DatasetEvent
    id: Incomplete
    dataset_id: Incomplete
    dataset_uri: Incomplete
    extra: Incomplete
    source_task_id: Incomplete
    source_dag_id: Incomplete
    source_run_id: Incomplete
    source_map_index: Incomplete
    created_dagruns: Incomplete
    timestamp: Incomplete

class DatasetEventCollection(NamedTuple):
    dataset_events: list[DatasetEvent]
    total_entries: int

class DatasetEventCollectionSchema(Schema):
    dataset_events: Incomplete
    total_entries: Incomplete

class CreateDatasetEventSchema(Schema):
    dataset_uri: Incomplete
    extra: Incomplete

dataset_event_schema: Incomplete
dataset_event_collection_schema: Incomplete
create_dataset_event_schema: Incomplete

class QueuedEvent(NamedTuple):
    uri: str
    dag_id: str
    created_at: datetime

class QueuedEventSchema(Schema):
    uri: Incomplete
    dag_id: Incomplete
    created_at: Incomplete

class QueuedEventCollection(NamedTuple):
    queued_events: list[QueuedEvent]
    total_entries: int

class QueuedEventCollectionSchema(Schema):
    queued_events: Incomplete
    total_entries: Incomplete

queued_event_schema: Incomplete
queued_event_collection_schema: Incomplete
