from _typeshed import Incomplete
from airflow.models.dagwarning import DagWarning as DagWarning
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class DagWarningSchema(SQLAlchemySchema):
    class Meta:
        model = DagWarning
    dag_id: Incomplete
    warning_type: Incomplete
    message: Incomplete
    timestamp: Incomplete

class DagWarningCollection(NamedTuple):
    dag_warnings: list[DagWarning]
    total_entries: int

class DagWarningCollectionSchema(Schema):
    dag_warnings: Incomplete
    total_entries: Incomplete

dag_warning_schema: Incomplete
dag_warning_collection_schema: Incomplete
