from _typeshed import Incomplete
from airflow.migrations.db_types import StringID as StringID, TIMESTAMP as TIMESTAMP
from airflow.migrations.utils import get_mssql_table_constraints as get_mssql_table_constraints

ID_LEN: int
revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def tables(for_downgrade: bool = False) -> None: ...
def upgrade() -> None: ...
def downgrade() -> None: ...
