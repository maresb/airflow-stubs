import airflow.utils.timezone as timezone
import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.utils.sqlalchemy import ExtendedJSON as ExtendedJSON, UtcDateTime as UtcDateTime
from typing import ClassVar

TYPE_CHECKING: bool

class DbCallbackRequest(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    created_at: Incomplete
    priority_weight: Incomplete
    callback_data: Incomplete
    callback_type: Incomplete
    processor_subdir: Incomplete
    def __init__(self, priority_weight, callback) -> None: ...
    def get_callback_request(self) -> CallbackRequest: ...
