import airflow.settings as settings
import sqlalchemy.orm.decl_api
import sqlalchemy.orm.instrumentation
import sqlalchemy.orm.mapper
import sqlalchemy.sql.schema
from _typeshed import Incomplete
from airflow.models.dagbag import DagBag as DagBag
from typing import ClassVar

revision: str
down_revision: str
branch_labels: None
depends_on: None
airflow_version: str
BATCH_SIZE: int

class TaskInstance(sqlalchemy.orm.decl_api.Base):
    __tablename__: ClassVar[str] = ...
    _sa_class_manager: ClassVar[sqlalchemy.orm.instrumentation.ClassManager] = ...
    __table__: ClassVar[sqlalchemy.sql.schema.Table] = ...
    __mapper__: ClassVar[sqlalchemy.orm.mapper.Mapper] = ...
    task_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    max_tries: Incomplete
    try_number: Incomplete
    def __init__(self, **kwargs) -> None: ...
def upgrade(): ...
def downgrade(): ...
