from _typeshed import Incomplete
from airflow.models.connection import Connection as Connection
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class ConnectionCollectionItemSchema(SQLAlchemySchema):
    class Meta:
        model = Connection
    connection_id: Incomplete
    conn_type: Incomplete
    description: Incomplete
    host: Incomplete
    login: Incomplete
    schema: Incomplete
    port: Incomplete

class ConnectionSchema(ConnectionCollectionItemSchema):
    password: Incomplete
    extra: Incomplete
    @staticmethod
    def serialize_extra(obj: Connection): ...
    @staticmethod
    def deserialize_extra(value): ...

class ConnectionCollection(NamedTuple):
    connections: list[Connection]
    total_entries: int

class ConnectionCollectionSchema(Schema):
    connections: Incomplete
    total_entries: Incomplete

class ConnectionTestSchema(Schema):
    status: Incomplete
    message: Incomplete

connection_schema: Incomplete
connection_collection_item_schema: Incomplete
connection_collection_schema: Incomplete
connection_test_schema: Incomplete
