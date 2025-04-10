from _typeshed import Incomplete
from airflow.utils.types import DagRunType as DagRunType

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str
Base: Incomplete

class DagRun(Base):
    __tablename__: str
    id: Incomplete
    run_id: Incomplete
    run_type: Incomplete

def upgrade() -> None: ...
def downgrade() -> None: ...
