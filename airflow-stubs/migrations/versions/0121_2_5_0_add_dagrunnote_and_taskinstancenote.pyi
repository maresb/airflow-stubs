from _typeshed import Incomplete
from airflow.migrations.db_types import StringID as StringID
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
