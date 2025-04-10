from _typeshed import Incomplete
from airflow.migrations.db_types import TIMESTAMP as TIMESTAMP

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def is_table_empty(conn, table_name): ...
def get_table_constraints(conn, table_name) -> dict[tuple[str, str], list[str]]: ...
def drop_column_constraints(operator, column_name, constraint_dict) -> None: ...
def create_constraints(operator, column_name, constraint_dict) -> None: ...
def recreate_mssql_ts_column(conn, op, table_name, column_name) -> None: ...
def alter_mssql_datetime_column(conn, op, table_name, column_name, nullable) -> None: ...
def upgrade() -> None: ...
def downgrade() -> None: ...
