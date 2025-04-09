import pandas as pd
from _typeshed import Incomplete
from airflow.serialization.serde import U as U
from airflow.utils.module_loading import qualname as qualname

serializers: Incomplete
deserializers = serializers
__version__: int

def serialize(o: object) -> tuple[U, str, int, bool]: ...
def deserialize(classname: str, version: int, data: object) -> pd.DataFrame: ...
