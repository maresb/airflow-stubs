import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.utils.session import create_session as create_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from typing import ClassVar

revision: str
down_revision: str
branch_labels: None
depends_on: None
airflow_version: str
ID_LEN: int

class TaskInstance(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    task_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    pool: Incomplete
    def __init__(self, **kwargs) -> None: ...
def upgrade(): ...
def downgrade(): ...
