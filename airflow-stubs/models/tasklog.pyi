from _typeshed import Incomplete
from airflow.models.base import Base as Base
from airflow.utils import timezone as timezone
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

class LogTemplate(Base):
    __tablename__: str
    id: Incomplete
    filename: Incomplete
    elasticsearch_id: Incomplete
    created_at: Incomplete
