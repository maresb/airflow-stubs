import datetime
from airflow.serialization.serializers.timezone import deserialize_timezone as deserialize_timezone, serialize_timezone as serialize_timezone
from airflow.utils.module_loading import qualname as qualname
from airflow.utils.timezone import parse_timezone as parse_timezone

TYPE_CHECKING: bool
__version__: int
serializers: list
deserializers: list
TIMESTAMP: str
TIMEZONE: str
def serialize(o: object) -> tuple[U, str, int, bool]: ...
def deserialize(classname: str, version: int, data: dict | str) -> datetime.date | datetime.timedelta: ...
