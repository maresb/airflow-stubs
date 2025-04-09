from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.models.base import Base as Base, StringID as StringID
from airflow.utils import timezone as timezone
from airflow.utils.retries import retry_db_transaction as retry_db_transaction
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from enum import Enum
from sqlalchemy.orm import Session as Session

class DagWarning(Base):
    dag_id: Incomplete
    warning_type: Incomplete
    message: Incomplete
    timestamp: Incomplete
    __tablename__: str
    __table_args__: Incomplete
    def __init__(self, dag_id: str, error_type: str, message: str, **kwargs) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    @classmethod
    def purge_inactive_dag_warnings(cls, session: Session = ...) -> None: ...

class DagWarningType(str, Enum):
    NONEXISTENT_POOL = 'non-existent pool'
