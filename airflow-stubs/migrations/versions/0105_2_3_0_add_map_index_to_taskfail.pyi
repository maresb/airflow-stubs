from _typeshed import Incomplete
from airflow.migrations.db_types import StringID as StringID, TIMESTAMP as TIMESTAMP
from sqlalchemy.sql import ColumnElement as ColumnElement, Update as Update

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str
ID_LEN: int

def tables() -> None: ...
def upgrade() -> None: ...
def downgrade() -> None: ...
