import sqlalchemy as sa
from _typeshed import Incomplete
from airflow.models.trigger import Trigger as Trigger
from airflow.serialization.serialized_objects import BaseSerialization as BaseSerialization
from airflow.utils.sqlalchemy import ExtendedJSON as ExtendedJSON

revision: str
down_revision: str
branch_labels: Incomplete
depends_on: Incomplete
airflow_version: str

def get_session() -> sa.orm.Session: ...
def upgrade() -> None: ...
def downgrade() -> None: ...
