import airflow as airflow
import typing
from airflow.configuration import conf as conf
from airflow.stats import Stats as Stats
from airflow.utils.module_loading import import_string as import_string, iter_namespace as iter_namespace, qualname as qualname
from typing import Any, U

TYPE_CHECKING: bool
MAX_RECURSION_DEPTH: int
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
T: typing.TypeVar
def encode(cls: str, version: int, data: T) -> dict[str, str | int | T]: ...
def decode(d: dict[str, Any]) -> tuple[str, int, Any]: ...
def serialize(o: object, depth: int = ...) -> U | None: ...
def deserialize(o: T | None, full: bool = ..., type_hint: Any = ...) -> object: ...
