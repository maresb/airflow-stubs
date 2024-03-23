import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import ClassVar

COLLATION_ARGS: dict
ID_LEN: int

class SlaMiss(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    __table_args__: ClassVar[tuple] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    task_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    email_sent: Incomplete
    timestamp: Incomplete
    description: Incomplete
    notification_sent: Incomplete
    def __init__(self, **kwargs) -> None: ...
