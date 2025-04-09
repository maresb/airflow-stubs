from airflow import DAG as DAG
from airflow.models.taskinstance import PAST_DEPENDS_MET as PAST_DEPENDS_MET, TaskInstance as TaskInstance
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep, TIDepStatus as TIDepStatus
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from airflow.utils.task_group import MappedTaskGroup as MappedTaskGroup
from sqlalchemy.orm import Session as Session
from sqlalchemy.sql.expression import ColumnOperators as ColumnOperators
from typing import Iterator, NamedTuple

class _UpstreamTIStates(NamedTuple):
    success: int
    skipped: int
    failed: int
    upstream_failed: int
    removed: int
    done: int
    success_setup: int
    skipped_setup: int
    @classmethod
    def calculate(cls, finished_upstreams: Iterator[TaskInstance]) -> _UpstreamTIStates: ...

class TriggerRuleDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    IS_TASK_DEP: bool
