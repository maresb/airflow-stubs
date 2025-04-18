from _typeshed import Incomplete

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def get_table_constraints(conn, table_name) -> dict[tuple[str, str], list[str]]: ...
def drop_column_constraints(operator, column_name, constraint_dict) -> None: ...
def create_constraints(operator, column_name, constraint_dict) -> None: ...
def upgrade() -> None: ...
def downgrade() -> None: ...
