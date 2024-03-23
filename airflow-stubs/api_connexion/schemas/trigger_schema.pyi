import airflow.models.trigger
import collections
import marshmallow_sqlalchemy.schema
from airflow.models.trigger import Trigger as Trigger
from typing import ClassVar

class TriggerSchema(marshmallow_sqlalchemy.schema.SQLAlchemySchema):
    class Meta:
        model: ClassVar[type[airflow.models.trigger.Trigger]] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    opts: ClassVar[marshmallow_sqlalchemy.schema.SQLAlchemySchemaOpts] = ...
    _declared_fields: ClassVar[dict] = ...
    _hooks: ClassVar[collections.defaultdict] = ...