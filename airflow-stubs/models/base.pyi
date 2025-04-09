from _typeshed import Incomplete
from airflow.configuration import conf as conf
from sqlalchemy import String
from typing import Any

SQL_ALCHEMY_SCHEMA: Incomplete
naming_convention: Incomplete
metadata: Incomplete
mapper_registry: Incomplete
Base = Any
ID_LEN: int

def get_id_collation_args(): ...

COLLATION_ARGS: dict[str, Any]

def StringID(*, length=..., **kwargs) -> String: ...

class TaskInstanceDependencies(Base):
    __abstract__: bool
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
