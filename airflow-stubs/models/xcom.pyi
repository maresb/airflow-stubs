import datetime
import pendulum
from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.configuration import conf as conf
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.base import COLLATION_ARGS as COLLATION_ARGS, ID_LEN as ID_LEN, TaskInstanceDependencies as TaskInstanceDependencies
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.utils import timezone as timezone
from airflow.utils.db import LazySelectSequence as LazySelectSequence
from airflow.utils.helpers import exactly_one as exactly_one, is_container as is_container
from airflow.utils.json import XComDecoder as XComDecoder, XComEncoder as XComEncoder
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from airflow.utils.xcom import MAX_XCOM_SIZE as MAX_XCOM_SIZE, XCOM_RETURN_KEY as XCOM_RETURN_KEY
from sqlalchemy.engine import Row as Row
from sqlalchemy.orm import Query as Query, Session as Session
from sqlalchemy.sql.expression import Select as Select, TextClause as TextClause
from typing import Any, Iterable, overload

log: Incomplete

class BaseXCom(TaskInstanceDependencies, LoggingMixin):
    __tablename__: str
    dag_run_id: Incomplete
    task_id: Incomplete
    map_index: Incomplete
    key: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    value: Incomplete
    timestamp: Incomplete
    __table_args__: Incomplete
    dag_run: Incomplete
    execution_date: Incomplete
    def init_on_load(self) -> None: ...
    @overload
    @classmethod
    def set(cls, key: str, value: Any, *, dag_id: str, task_id: str, run_id: str, map_index: int = -1, session: Session = ...) -> None: ...
    @overload
    @classmethod
    def set(cls, key: str, value: Any, task_id: str, dag_id: str, execution_date: datetime.datetime, session: Session = ...) -> None: ...
    @staticmethod
    def get_value(*, ti_key: TaskInstanceKey, key: str | None = None, session: Session = ...) -> Any: ...
    @overload
    @staticmethod
    def get_one(*, key: str | None = None, dag_id: str | None = None, task_id: str | None = None, run_id: str | None = None, map_index: int | None = None, session: Session = ...) -> Any | None: ...
    @overload
    @staticmethod
    def get_one(execution_date: datetime.datetime, key: str | None = None, task_id: str | None = None, dag_id: str | None = None, include_prior_dates: bool = False, session: Session = ...) -> Any | None: ...
    @overload
    @staticmethod
    def get_many(*, run_id: str, key: str | None = None, task_ids: str | Iterable[str] | None = None, dag_ids: str | Iterable[str] | None = None, map_indexes: int | Iterable[int] | None = None, include_prior_dates: bool = False, limit: int | None = None, session: Session = ...) -> Query: ...
    @overload
    @staticmethod
    def get_many(execution_date: datetime.datetime, key: str | None = None, task_ids: str | Iterable[str] | None = None, dag_ids: str | Iterable[str] | None = None, map_indexes: int | Iterable[int] | None = None, include_prior_dates: bool = False, limit: int | None = None, session: Session = ...) -> Query: ...
    @classmethod
    def delete(cls, xcoms: XCom | Iterable[XCom], session: Session) -> None: ...
    @staticmethod
    def purge(xcom: XCom, session: Session) -> None: ...
    @overload
    @staticmethod
    def clear(*, dag_id: str, task_id: str, run_id: str, map_index: int | None = None, session: Session = ...) -> None: ...
    @overload
    @staticmethod
    def clear(execution_date: pendulum.DateTime, dag_id: str, task_id: str, session: Session = ...) -> None: ...
    @staticmethod
    def serialize_value(value: Any, *, key: str | None = None, task_id: str | None = None, dag_id: str | None = None, run_id: str | None = None, map_index: int | None = None) -> Any: ...
    @staticmethod
    def deserialize_value(result: XCom) -> Any: ...
    def orm_deserialize_value(self) -> Any: ...

class LazyXComSelectSequence(LazySelectSequence[Any]): ...

def resolve_xcom_backend() -> type[BaseXCom]: ...
XCom = BaseXCom
