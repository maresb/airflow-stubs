from airflow.migrations.utils import get_mssql_table_constraints as get_mssql_table_constraints

revision: str
down_revision: str
branch_labels: None
depends_on: None
airflow_version: str
def upgrade(): ...
def downgrade(): ...
