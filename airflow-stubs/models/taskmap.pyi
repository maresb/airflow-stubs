import enum
from _typeshed import Incomplete
from airflow.models.base import COLLATION_ARGS as COLLATION_ARGS, ID_LEN as ID_LEN, TaskInstanceDependencies as TaskInstanceDependencies
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.utils.sqlalchemy import ExtendedJSON as ExtendedJSON
from typing import Any, Collection

class TaskMapVariant(enum.Enum):
    DICT = 'dict'
    LIST = 'list'

class TaskMap(TaskInstanceDependencies):
    __tablename__: str
    dag_id: Incomplete
    task_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    length: Incomplete
    keys: Incomplete
    __table_args__: Incomplete
    def __init__(self, dag_id: str, task_id: str, run_id: str, map_index: int, length: int, keys: list[Any] | None) -> None: ...
    @classmethod
    def from_task_instance_xcom(cls, ti: TaskInstance | TaskInstancePydantic, value: Collection) -> TaskMap: ...
    @property
    def variant(self) -> TaskMapVariant: ...
