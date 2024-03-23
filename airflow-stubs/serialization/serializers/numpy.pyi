from airflow.utils.module_loading import import_string as import_string, qualname as qualname
from typing import Any

TYPE_CHECKING: bool
serializers: list
deserializers: list
__version__: int
def serialize(o: object) -> tuple[U, str, int, bool]: ...
def deserialize(classname: str, version: int, data: str) -> Any: ...
