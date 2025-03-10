import collections
import marshmallow.schema
from typing import ClassVar

class DagSourceSchema(marshmallow.schema.Schema):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    opts: ClassVar[marshmallow.schema.SchemaOpts] = ...
    _declared_fields: ClassVar[dict] = ...
    _hooks: ClassVar[collections.defaultdict] = ...
dag_source_schema: DagSourceSchema
