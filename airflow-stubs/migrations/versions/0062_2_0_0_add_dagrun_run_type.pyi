import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.utils.types import DagRunType as DagRunType
from typing import ClassVar

revision: str
down_revision: str
branch_labels: None
depends_on: None
airflow_version: str

class DagRun(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    id: Incomplete
    run_id: Incomplete
    run_type: Incomplete
    def __init__(self, **kwargs) -> None: ...
def upgrade(): ...
def downgrade(): ...
