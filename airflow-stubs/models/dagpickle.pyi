from _typeshed import Incomplete
from airflow.models.base import Base as Base
from airflow.models.dag import DAG as DAG
from airflow.utils import timezone as timezone
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

class DagPickle(Base):
    id: Incomplete
    pickle: Incomplete
    created_dttm: Incomplete
    pickle_hash: Incomplete
    __tablename__: str
    dag_id: Incomplete
    def __init__(self, dag: DAG) -> None: ...
