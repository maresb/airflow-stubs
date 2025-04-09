from _typeshed import Incomplete
from airflow.models import XCom as XCom
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class XComCollectionItemSchema(SQLAlchemySchema):
    class Meta:
        model = XCom
    key: Incomplete
    timestamp: Incomplete
    execution_date: Incomplete
    map_index: Incomplete
    task_id: Incomplete
    dag_id: Incomplete

class XComSchemaNative(XComCollectionItemSchema):
    value: Incomplete

class XComSchemaString(XComCollectionItemSchema):
    value: Incomplete

class XComCollection(NamedTuple):
    xcom_entries: list[XCom]
    total_entries: int

class XComCollectionSchema(Schema):
    xcom_entries: Incomplete
    total_entries: Incomplete

xcom_schema_native: Incomplete
xcom_schema_string: Incomplete
xcom_collection_item_schema: Incomplete
xcom_collection_schema: Incomplete
