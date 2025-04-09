from _typeshed import Incomplete
from airflow.models.errors import ParseImportError as ParseImportError
from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemySchema
from typing import NamedTuple

class ImportErrorSchema(SQLAlchemySchema):
    class Meta:
        model = ParseImportError
    import_error_id: Incomplete
    timestamp: Incomplete
    filename: Incomplete
    stack_trace: Incomplete

class ImportErrorCollection(NamedTuple):
    import_errors: list[ParseImportError]
    total_entries: int

class ImportErrorCollectionSchema(Schema):
    import_errors: Incomplete
    total_entries: Incomplete

import_error_schema: Incomplete
import_error_collection_schema: Incomplete
