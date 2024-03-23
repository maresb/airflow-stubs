from airflow.utils.module_loading import qualname as qualname

TYPE_CHECKING: bool
serializers: list
__version__: int
deserializers: list
def serialize(o: object) -> tuple[U, str, int, bool]: ...
