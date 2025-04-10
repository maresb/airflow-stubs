from _typeshed import Incomplete
from airflow.security import permissions as permissions
from airflow.www.app import cached_app as cached_app

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
