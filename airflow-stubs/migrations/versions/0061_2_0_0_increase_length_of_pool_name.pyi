from _typeshed import Incomplete
from airflow.models.base import COLLATION_ARGS as COLLATION_ARGS

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
