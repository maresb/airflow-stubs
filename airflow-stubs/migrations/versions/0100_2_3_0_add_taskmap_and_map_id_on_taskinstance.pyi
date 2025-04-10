from _typeshed import Incomplete
from airflow.models.base import StringID as StringID
from airflow.utils.sqlalchemy import ExtendedJSON as ExtendedJSON

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
