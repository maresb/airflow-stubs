from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep, TIDepStatus as TIDepStatus
from airflow.utils.state import State as State, TaskInstanceState as TaskInstanceState
from sqlalchemy.orm import Session as Session

class MappedTaskUpstreamDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    IS_TASK_DEP: bool
