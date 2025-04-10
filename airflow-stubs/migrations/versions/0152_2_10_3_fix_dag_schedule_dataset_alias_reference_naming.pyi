from _typeshed import Incomplete
from alembic.operations.base import BatchOperations as BatchOperations
from sqlalchemy.sql.elements import conv as conv

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def upgrade() -> None: ...
def downgrade() -> None: ...
