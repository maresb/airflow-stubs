from _typeshed import Incomplete
from airflow.models.log import Log as Log
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class EventLogSchema(SQLAlchemySchema):
    class Meta:
        model = Log
    id: Incomplete
    dttm: Incomplete
    dag_id: Incomplete
    task_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    try_number: Incomplete
    event: Incomplete
    execution_date: Incomplete
    owner: Incomplete
    extra: Incomplete

class EventLogCollection(NamedTuple):
    event_logs: list[Log]
    total_entries: int

class EventLogCollectionSchema(Schema):
    event_logs: Incomplete
    total_entries: Incomplete

event_log_schema: Incomplete
event_log_collection_schema: Incomplete
