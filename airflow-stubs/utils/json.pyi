import json
from airflow.serialization.serde import CLASSNAME as CLASSNAME, DATA as DATA, SCHEMA_ID as SCHEMA_ID, deserialize as deserialize, serialize as serialize
from airflow.utils.timezone import convert_to_utc as convert_to_utc, is_naive as is_naive
from flask.json.provider import JSONProvider
from typing import Any

class AirflowJsonProvider(JSONProvider):
    ensure_ascii: bool
    sort_keys: bool
    def dumps(self, obj, **kwargs): ...
    def loads(self, s: str | bytes, **kwargs): ...

class WebEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...

class XComEncoder(json.JSONEncoder):
    def default(self, o: object) -> Any: ...
    def encode(self, o: Any) -> str: ...

class XComDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs) -> None: ...
    def object_hook(self, dct: dict) -> object: ...
    @staticmethod
    def orm_object_hook(dct: dict) -> object: ...
AirflowJsonEncoder = WebEncoder
