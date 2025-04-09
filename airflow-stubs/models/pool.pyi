from _typeshed import Incomplete
from airflow.exceptions import AirflowException as AirflowException, PoolNotFound as PoolNotFound
from airflow.models.base import Base as Base
from airflow.ti_deps.dependencies_states import EXECUTION_STATES as EXECUTION_STATES
from airflow.typing_compat import TypedDict as TypedDict
from airflow.utils.db import exists_query as exists_query
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import with_row_locks as with_row_locks
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from sqlalchemy.orm.session import Session as Session
from typing import Any

class PoolStats(TypedDict):
    total: int
    running: int
    deferred: int
    queued: int
    open: int
    scheduled: int

class Pool(Base):
    __tablename__: str
    id: Incomplete
    pool: Incomplete
    slots: Incomplete
    description: Incomplete
    include_deferred: Incomplete
    DEFAULT_POOL_NAME: str
    @staticmethod
    def get_pools(session: Session = ...) -> list[Pool]: ...
    @staticmethod
    def get_pool(pool_name: str, session: Session = ...) -> Pool | None: ...
    @staticmethod
    def get_default_pool(session: Session = ...) -> Pool | None: ...
    @staticmethod
    def is_default_pool(id: int, session: Session = ...) -> bool: ...
    @staticmethod
    def create_or_update_pool(name: str, slots: int, description: str, include_deferred: bool, session: Session = ...) -> Pool: ...
    @staticmethod
    def delete_pool(name: str, session: Session = ...) -> Pool: ...
    @staticmethod
    def slots_stats(*, lock_rows: bool = False, session: Session = ...) -> dict[str, PoolStats]: ...
    def to_json(self) -> dict[str, Any]: ...
    def occupied_slots(self, session: Session = ...) -> int: ...
    def get_occupied_states(self): ...
    def running_slots(self, session: Session = ...) -> int: ...
    def queued_slots(self, session: Session = ...) -> int: ...
    def scheduled_slots(self, session: Session = ...) -> int: ...
    def deferred_slots(self, session: Session = ...) -> int: ...
    def open_slots(self, session: Session = ...) -> float: ...
