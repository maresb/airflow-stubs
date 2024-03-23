import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.models.base import StringID as StringID
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import ClassVar

class TaskFail(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    __table_args__: ClassVar[tuple] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    duration: Incomplete
    dag_run: Incomplete
    def __init__(self, ti) -> None: ...
