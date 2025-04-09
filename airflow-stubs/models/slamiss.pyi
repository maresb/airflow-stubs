from _typeshed import Incomplete
from airflow.models.base import Base as Base, COLLATION_ARGS as COLLATION_ARGS, ID_LEN as ID_LEN
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

class SlaMiss(Base):
    __tablename__: str
    task_id: Incomplete
    dag_id: Incomplete
    execution_date: Incomplete
    email_sent: Incomplete
    timestamp: Incomplete
    description: Incomplete
    notification_sent: Incomplete
    __table_args__: Incomplete
