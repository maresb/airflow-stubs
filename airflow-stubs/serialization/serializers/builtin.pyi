from airflow.utils.module_loading import qualname as qualname

TYPE_CHECKING: bool
__version__: int
serializers: list
deserializers: list
stringifiers: list
def serialize(o: object) -> tuple[U, str, int, bool]: ...
def deserialize(classname: str, version: int, data: list) -> tuple | set | frozenset: ...
def stringify(classname: str, version: int, data: list) -> str: ...
