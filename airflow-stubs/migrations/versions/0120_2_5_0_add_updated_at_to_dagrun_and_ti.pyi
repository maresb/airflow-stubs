from _typeshed import Incomplete
from airflow.migrations.db_types import TIMESTAMP as TIMESTAMP

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
