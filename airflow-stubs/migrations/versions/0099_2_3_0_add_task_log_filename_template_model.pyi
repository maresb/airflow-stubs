from airflow.migrations.utils import disable_sqlite_fkeys as disable_sqlite_fkeys
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

revision: str
down_revision: str
branch_labels: None
depends_on: None
airflow_version: str
def upgrade(): ...
def downgrade(): ...
