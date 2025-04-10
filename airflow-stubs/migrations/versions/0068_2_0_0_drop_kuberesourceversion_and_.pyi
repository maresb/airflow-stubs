from _typeshed import Incomplete

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str
WORKER_UUID_TABLE: str
WORKER_RESOURCEVERSION_TABLE: str

def upgrade() -> None: ...
def downgrade() -> None: ...
