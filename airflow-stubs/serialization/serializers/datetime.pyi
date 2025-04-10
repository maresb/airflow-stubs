import datetime
from _typeshed import Incomplete
from airflow.serialization.serde import U as U
from airflow.utils.module_loading import qualname as qualname
from airflow.utils.timezone import parse_timezone as parse_timezone

__version__: int
serializers: Incomplete
deserializers = serializers
TIMESTAMP: str
TIMEZONE: str

def serialize(o: object) -> tuple[U, str, int, bool]: ...
def deserialize(classname: str, version: int, data: dict | str) -> datetime.date | datetime.timedelta: ...
