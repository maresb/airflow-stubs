import attrs
import enum
from _typeshed import Incomplete
from airflow import settings as settings
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import import_all_models as import_all_models
from airflow.models.connection import Connection as Connection
from airflow.typing_compat import Self as Self
from airflow.utils import helpers as helpers
from airflow.utils.session import NEW_SESSION as NEW_SESSION, create_session as create_session, provide_session as provide_session
from airflow.utils.task_instance_session import get_current_task_instance_session as get_current_task_instance_session
from sqlalchemy.engine import Row as Row
from sqlalchemy.orm import Query as Query, Session as Session
from sqlalchemy.sql.elements import ClauseElement as ClauseElement, TextClause as TextClause
from sqlalchemy.sql.selectable import Select as Select
from typing import Any, Generator, Iterable, Iterator, Protocol, Sequence, TypeVar, overload

class MappedClassProtocol(Protocol):
    __tablename__: str
T = TypeVar('T')
log: Incomplete

def merge_conn(conn: Connection, session: Session = ...): ...
def add_default_pool_if_not_exists(session: Session = ...): ...
def create_default_connections(session: Session = ...): ...
def initdb(session: Session = ..., load_connections: bool = True, use_migration_files: bool = False): ...
def check_migrations(timeout) -> None: ...
def check_and_run_migrations() -> None: ...
def synchronize_log_template(*, session: Session = ...) -> None: ...
def check_conn_id_duplicates(session: Session) -> Iterable[str]: ...
def check_username_duplicates(session: Session) -> Iterable[str]: ...
def reflect_tables(tables: list[MappedClassProtocol | str] | None, session): ...
def check_table_for_duplicates(*, session: Session, table_name: str, uniqueness: list[str], version: str) -> Iterable[str]: ...
def check_conn_type_null(session: Session) -> Iterable[str]: ...
def check_run_id_null(session: Session) -> Iterable[str]: ...
def check_bad_references(session: Session) -> Iterable[str]: ...
def print_happy_cat(message) -> None: ...
def upgradedb(*, to_revision: str | None = None, from_revision: str | None = None, show_sql_only: bool = False, reserialize_dags: bool = True, session: Session = ..., use_migration_files: bool = False): ...
def resetdb(session: Session = ..., skip_init: bool = False, use_migration_files: bool = False): ...
def bootstrap_dagbag(session: Session = ...): ...
def downgrade(*, to_revision, from_revision: Incomplete | None = None, show_sql_only: bool = False, session: Session = ...): ...
def drop_airflow_models(connection) -> None: ...
def drop_airflow_moved_tables(connection) -> None: ...
def check(session: Session = ...): ...

class DBLocks(enum.IntEnum):
    MIGRATIONS = ...
    SCHEDULER_CRITICAL_SECTION = ...

def create_global_lock(session: Session, lock: DBLocks, lock_timeout: int = 1800) -> Generator[None, None, None]: ...
def compare_type(context, inspected_column, metadata_column, inspected_type, metadata_type): ...
def compare_server_default(context, inspected_column, metadata_column, inspected_default, metadata_default, rendered_metadata_default): ...
def get_sqla_model_classes(): ...
def get_query_count(query_stmt: Select, *, session: Session) -> int: ...
def check_query_exists(query_stmt: Select, *, session: Session) -> bool: ...
def exists_query(*where: ClauseElement, session: Session) -> bool: ...

@attrs.define(slots=True)
class LazySelectSequence(Sequence[T]):
    @classmethod
    def from_select(cls, select: Select, *, order_by: Sequence[ClauseElement], session: Session | None = None) -> Self: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __reversed__(self) -> Iterator[T]: ...
    def __iter__(self) -> Iterator[T]: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: int) -> T: ...
    @overload
    def __getitem__(self, key: slice) -> Sequence[T]: ...
