from _typeshed import Incomplete
from airflow import settings as settings
from airflow.models import DagBag as DagBag

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str
Base: Incomplete
BATCH_SIZE: int

class TaskInstance(Base):
    __tablename__: str
    task_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    max_tries: Incomplete
    try_number: Incomplete

def upgrade() -> None: ...
def downgrade() -> None: ...
