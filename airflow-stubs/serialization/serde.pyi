from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.stats import Stats as Stats
from airflow.utils.module_loading import import_string as import_string, iter_namespace as iter_namespace, qualname as qualname
from typing import Any, TypeVar

log: Incomplete
MAX_RECURSION_DEPTH: Incomplete
CLASSNAME: str
VERSION: str
DATA: str
SCHEMA_ID: str
CACHE: str
OLD_TYPE: str
OLD_SOURCE: str
OLD_DATA: str
OLD_DICT: str
DEFAULT_VERSION: int
T = TypeVar('T', bool, float, int, dict, list, str, tuple, set)
U = bool | float | int | dict | list | str | tuple | set
S = list | tuple | set

def encode(cls, version: int, data: T) -> dict[str, str | int | T]: ...
def decode(d: dict[str, Any]) -> tuple[str, int, Any]: ...
def serialize(o: object, depth: int = 0) -> U | None: ...
def deserialize(o: T | None, full: bool = True, type_hint: Any = None) -> object: ...
