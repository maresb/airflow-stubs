import enum
from _typeshed import Incomplete
from airflow.typing_compat import TypedDict as TypedDict
from datetime import datetime

class ArgNotSet: ...

NOTSET: Incomplete

class AttributeRemoved:
    attribute_name: Incomplete
    def __init__(self, attribute_name: str) -> None: ...
    def __getattr__(self, item): ...

class DagRunType(str, enum.Enum):
    BACKFILL_JOB = 'backfill'
    SCHEDULED = 'scheduled'
    MANUAL = 'manual'
    DATASET_TRIGGERED = 'dataset_triggered'
    def generate_run_id(self, logical_date: datetime) -> str: ...
    @staticmethod
    def from_run_id(run_id: str) -> DagRunType: ...

class EdgeInfoType(TypedDict):
    label: str | None
