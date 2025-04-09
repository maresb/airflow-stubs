from _typeshed import Incomplete
from airflow.models.base import Base as Base, StringID as StringID
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.utils import timezone as timezone
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

class Log(Base):
    __tablename__: str
    id: Incomplete
    dttm: Incomplete
    dag_id: Incomplete
    task_id: Incomplete
    map_index: Incomplete
    event: Incomplete
    execution_date: Incomplete
    run_id: Incomplete
    owner: Incomplete
    owner_display_name: Incomplete
    extra: Incomplete
    try_number: Incomplete
    __table_args__: Incomplete
    def __init__(self, event, task_instance: TaskInstance | TaskInstanceKey | None = None, owner: Incomplete | None = None, owner_display_name: Incomplete | None = None, extra: Incomplete | None = None, **kwargs) -> None: ...
