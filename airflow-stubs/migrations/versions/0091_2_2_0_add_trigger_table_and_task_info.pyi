from airflow.utils.sqlalchemy import ExtendedJSON as ExtendedJSON

revision: str
down_revision: str
branch_labels: None
depends_on: None
airflow_version: str
def upgrade(): ...
def downgrade(): ...
