from _typeshed import Incomplete
from airflow.models.dagcode import DagCode as DagCode

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
