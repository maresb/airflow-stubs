import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import ClassVar

class ImportError(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    timestamp: Incomplete
    filename: Incomplete
    stacktrace: Incomplete
    processor_subdir: Incomplete
    def __init__(self, **kwargs) -> None: ...
