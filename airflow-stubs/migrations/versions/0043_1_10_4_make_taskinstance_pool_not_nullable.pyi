from _typeshed import Incomplete
from airflow.utils.session import create_session as create_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str
Base: Incomplete
ID_LEN: int

class TaskInstance(Base):
    __tablename__: str
    task_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    pool: Incomplete

def upgrade() -> None: ...
def downgrade() -> None: ...
