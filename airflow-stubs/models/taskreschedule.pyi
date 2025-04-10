import datetime
from _typeshed import Incomplete
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.base import COLLATION_ARGS as COLLATION_ARGS, ID_LEN as ID_LEN, TaskInstanceDependencies as TaskInstanceDependencies
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime
from sqlalchemy.orm import Query as Query, Session as Session
from sqlalchemy.sql import Select as Select

class TaskReschedule(TaskInstanceDependencies):
    __tablename__: str
    id: Incomplete
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    try_number: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    duration: Incomplete
    reschedule_date: Incomplete
    __table_args__: Incomplete
    dag_run: Incomplete
    execution_date: Incomplete
    def __init__(self, task_id: str, dag_id: str, run_id: str, try_number: int, start_date: datetime.datetime, end_date: datetime.datetime, reschedule_date: datetime.datetime, map_index: int = -1) -> None: ...
    @classmethod
    def stmt_for_task_instance(cls, ti: TaskInstance | TaskInstancePydantic, *, try_number: int | None = None, descending: bool = False) -> Select: ...
    @staticmethod
    def query_for_task_instance(task_instance: TaskInstance, descending: bool = False, session: Session = ..., try_number: int | None = None) -> Query: ...
    @staticmethod
    def find_for_task_instance(task_instance: TaskInstance, session: Session = ..., try_number: int | None = None) -> list[TaskReschedule]: ...
