from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.exceptions import AirflowException as AirflowException, DagCodeNotFound as DagCodeNotFound
from airflow.models.base import Base as Base
from airflow.utils import timezone as timezone
from airflow.utils.file import correct_maybe_zipped as correct_maybe_zipped, open_maybe_zipped as open_maybe_zipped
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from sqlalchemy.orm import Session as Session
from typing import Collection, Iterable

log: Incomplete

class DagCode(Base):
    __tablename__: str
    fileloc_hash: Incomplete
    fileloc: Incomplete
    last_updated: Incomplete
    source_code: Incomplete
    def __init__(self, full_filepath: str, source_code: str | None = None) -> None: ...
    def sync_to_db(self, session: Session = ...) -> None: ...
    @classmethod
    def bulk_sync_to_db(cls, filelocs: Iterable[str], session: Session = ...) -> None: ...
    @classmethod
    def remove_deleted_code(cls, alive_dag_filelocs: Collection[str], processor_subdir: str, session: Session = ...) -> None: ...
    @classmethod
    def has_dag(cls, fileloc: str, session: Session = ...) -> bool: ...
    @classmethod
    def get_code_by_fileloc(cls, fileloc: str) -> str: ...
    @classmethod
    def code(cls, fileloc, session: Session = ...) -> str: ...
    @staticmethod
    def dag_fileloc_hash(full_filepath: str) -> int: ...
