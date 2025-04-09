from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState

class TaskNotRunningDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    def __eq__(self, other): ...
    def __hash__(self): ...
