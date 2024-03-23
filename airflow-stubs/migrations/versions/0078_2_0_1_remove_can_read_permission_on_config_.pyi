import airflow.security.permissions as permissions
from airflow.www.app import cached_app as cached_app

revision: str
down_revision: str
branch_labels: None
depends_on: None
airflow_version: str
def upgrade(): ...
def downgrade(): ...
