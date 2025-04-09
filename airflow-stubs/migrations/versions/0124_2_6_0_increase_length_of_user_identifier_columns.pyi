from _typeshed import Incomplete
from airflow.migrations.utils import get_mssql_table_constraints as get_mssql_table_constraints

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
