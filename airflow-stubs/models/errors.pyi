from _typeshed import Incomplete
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.base import Base as Base
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

class ParseImportError(Base):
    __tablename__: str
    id: Incomplete
    timestamp: Incomplete
    filename: Incomplete
    stacktrace: Incomplete
    processor_subdir: Incomplete

def __getattr__(name: str): ...
