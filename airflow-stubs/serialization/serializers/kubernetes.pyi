from _typeshed import Incomplete
from airflow.serialization.serde import U as U
from airflow.utils.module_loading import qualname as qualname

serializers: Incomplete
__version__: int
deserializers: list[type[object]]
log: Incomplete

def serialize(o: object) -> tuple[U, str, int, bool]: ...
