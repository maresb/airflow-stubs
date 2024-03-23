import airflow.models.dagwarning
import collections
import marshmallow.schema
import marshmallow_sqlalchemy.schema
from _typeshed import Incomplete
from airflow.models.dagwarning import DagWarning as DagWarning
from typing import ClassVar

class DagWarningSchema(marshmallow_sqlalchemy.schema.SQLAlchemySchema):
    class Meta:
        model: ClassVar[type[airflow.models.dagwarning.DagWarning]] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    opts: ClassVar[marshmallow_sqlalchemy.schema.SQLAlchemySchemaOpts] = ...
    _declared_fields: ClassVar[dict] = ...
    _hooks: ClassVar[collections.defaultdict] = ...

class DagWarningCollection(tuple):
    _fields: ClassVar[tuple] = ...
    _field_defaults: ClassVar[dict] = ...
    _fields_defaults: ClassVar[dict] = ...
    _field_types: ClassVar[dict] = ...
    dag_warnings: Incomplete
    total_entries: Incomplete
    def __init__(self, _cls, dag_warnings: list[DagWarning], total_entries: int) -> None: ...
    def __getnewargs__(self): ...

class DagWarningCollectionSchema(marshmallow.schema.Schema):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    opts: ClassVar[marshmallow.schema.SchemaOpts] = ...
    _declared_fields: ClassVar[dict] = ...
    _hooks: ClassVar[collections.defaultdict] = ...
dag_warning_schema: DagWarningSchema
dag_warning_collection_schema: DagWarningCollectionSchema
