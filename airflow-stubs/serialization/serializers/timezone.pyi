from airflow.utils.module_loading import qualname as qualname
from typing import Any

TYPE_CHECKING: bool
serializers: list
PY39: bool
deserializers: list
__version__: int
def serialize(o: object) -> tuple[U, str, int, bool]: ...
def deserialize(classname: str, version: int, data: object) -> Any: ...
