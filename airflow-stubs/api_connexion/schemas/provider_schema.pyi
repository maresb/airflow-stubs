from _typeshed import Incomplete
from airflow.typing_compat import TypedDict as TypedDict
from marshmallow import Schema
from typing import NamedTuple

class ProviderSchema(Schema):
    package_name: Incomplete
    description: Incomplete
    version: Incomplete

class Provider(TypedDict):
    package_name: str
    description: str
    version: str

class ProviderCollection(NamedTuple):
    providers: list[Provider]
    total_entries: int

class ProviderCollectionSchema(Schema):
    providers: Incomplete
    total_entries: Incomplete

provider_collection_schema: Incomplete
provider_schema: Incomplete
