from _typeshed import Incomplete
from airflow.models.pool import Pool as Pool
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class PoolSchema(SQLAlchemySchema):
    class Meta:
        model = Pool
    name: Incomplete
    slots: Incomplete
    occupied_slots: Incomplete
    running_slots: Incomplete
    queued_slots: Incomplete
    scheduled_slots: Incomplete
    open_slots: Incomplete
    deferred_slots: Incomplete
    description: Incomplete
    include_deferred: Incomplete
    @staticmethod
    def get_occupied_slots(obj: Pool) -> int: ...
    @staticmethod
    def get_running_slots(obj: Pool) -> int: ...
    @staticmethod
    def get_queued_slots(obj: Pool) -> int: ...
    @staticmethod
    def get_scheduled_slots(obj: Pool) -> int: ...
    @staticmethod
    def get_deferred_slots(obj: Pool) -> int: ...
    @staticmethod
    def get_open_slots(obj: Pool) -> float: ...

class PoolCollection(NamedTuple):
    pools: list[Pool]
    total_entries: int

class PoolCollectionSchema(Schema):
    pools: Incomplete
    total_entries: Incomplete

pool_collection_schema: Incomplete
pool_schema: Incomplete
