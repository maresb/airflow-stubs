from _typeshed import Incomplete
from airflow.migrations.db_types import StringID as StringID

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str
TABLE_NAME: str

def upgrade() -> None: ...
def downgrade() -> None: ...
