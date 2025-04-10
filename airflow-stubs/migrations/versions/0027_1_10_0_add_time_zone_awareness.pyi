from _typeshed import Incomplete
from airflow.exceptions import AirflowException as AirflowException

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
