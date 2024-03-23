import airflow.utils.timezone as timezone
import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils.retries import run_with_db_retries as run_with_db_retries
from airflow.utils.session import provide_session as provide_session
from airflow.utils.sqlalchemy import ExtendedJSON as ExtendedJSON, UtcDateTime as UtcDateTime, with_row_locks as with_row_locks
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from typing import ClassVar

TYPE_CHECKING: bool
NEW_SESSION: None

class Trigger(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    classpath: Incomplete
    kwargs: Incomplete
    created_date: Incomplete
    triggerer_id: Incomplete
    triggerer_job: Incomplete
    task_instance: Incomplete
    def __init__(self, classpath, kwargs, created_date: Incomplete | None = ...) -> None: ...
    @classmethod
    def from_object(cls, *args, **kwargs) -> Trigger: ...
    @classmethod
    def bulk_fetch(cls, *args, **kwargs) -> dict[int, Trigger]: ...
    @classmethod
    def clean_unused(cls, *args, **kwargs) -> None: ...
    @classmethod
    def submit_event(cls, *args, **kwargs) -> None: ...
    @classmethod
    def submit_failure(cls, *args, **kwargs) -> None: ...
    @classmethod
    def ids_for_triggerer(cls, *args, **kwargs) -> list[int]: ...
    @classmethod
    def assign_unassigned(cls, *args, **kwargs) -> None: ...
    @classmethod
    def get_sorted_triggers(cls, capacity, alive_triggerer_ids, session): ...
