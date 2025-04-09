from _typeshed import Incomplete
from airflow.models.base import StringID as StringID, TaskInstanceDependencies as TaskInstanceDependencies
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime

class TaskFail(TaskInstanceDependencies):
    __tablename__: str
    id: Incomplete
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    duration: Incomplete
    __table_args__: Incomplete
    dag_run: Incomplete
    def __init__(self, ti) -> None: ...
