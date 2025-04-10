from _typeshed import Incomplete
from airflow.serialization.serde import U as U
from airflow.utils.module_loading import qualname as qualname

__version__: int
serializers: Incomplete
deserializers = serializers
stringifiers = serializers

def serialize(o: object) -> tuple[U, str, int, bool]: ...
def deserialize(classname: str, version: int, data: list) -> tuple | set | frozenset: ...
def stringify(classname: str, version: int, data: list) -> str: ...
