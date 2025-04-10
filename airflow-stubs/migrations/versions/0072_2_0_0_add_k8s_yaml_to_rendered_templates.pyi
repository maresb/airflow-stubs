from _typeshed import Incomplete
from airflow.settings import json as json

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str
__tablename__: str
k8s_pod_yaml: Incomplete

def upgrade() -> None: ...
def downgrade() -> None: ...
