import airflow.utils.timezone as timezone
import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.models.base import StringID as StringID
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import ClassVar

class Log(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    __table_args__: ClassVar[tuple] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    dttm: Incomplete
    dag_id: Incomplete
    task_id: Incomplete
    map_index: Incomplete
    event: Incomplete
    execution_date: Incomplete
    owner: Incomplete
    owner_display_name: Incomplete
    extra: Incomplete
    def __init__(self, event, task_instance: Incomplete | None = ..., owner: Incomplete | None = ..., owner_display_name: Incomplete | None = ..., extra: Incomplete | None = ..., **kwargs) -> None: ...
