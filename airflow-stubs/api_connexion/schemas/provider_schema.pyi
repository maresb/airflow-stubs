import collections
import marshmallow.schema
from _typeshed import Incomplete
from typing import ClassVar

class ProviderSchema(marshmallow.schema.Schema):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    opts: ClassVar[marshmallow.schema.SchemaOpts] = ...
    _declared_fields: ClassVar[dict] = ...
    _hooks: ClassVar[collections.defaultdict] = ...

class Provider(dict):
    __total__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...

class ProviderCollection(tuple):
    _fields: ClassVar[tuple] = ...
    _field_defaults: ClassVar[dict] = ...
    _fields_defaults: ClassVar[dict] = ...
    _field_types: ClassVar[dict] = ...
    providers: Incomplete
    total_entries: Incomplete
    def __init__(self, _cls, providers: list[Provider], total_entries: int) -> None: ...
    def __getnewargs__(self): ...

class ProviderCollectionSchema(marshmallow.schema.Schema):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    opts: ClassVar[marshmallow.schema.SchemaOpts] = ...
    _declared_fields: ClassVar[dict] = ...
    _hooks: ClassVar[collections.defaultdict] = ...
provider_collection_schema: ProviderCollectionSchema
provider_schema: ProviderSchema
