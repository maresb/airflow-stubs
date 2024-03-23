from airflow.utils.module_loading import qualname as qualname

TYPE_CHECKING: bool
serializers: list
deserializers: list
stringifiers: list
__version__: int
def serialize(o: object) -> tuple[U, str, int, bool]: ...
def deserialize(classname: str, version: int, data: dict): ...
