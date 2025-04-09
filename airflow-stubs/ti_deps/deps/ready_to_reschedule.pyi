from _typeshed import Incomplete
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.models.taskreschedule import TaskReschedule as TaskReschedule
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils import timezone as timezone
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState

class ReadyToRescheduleDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    IS_TASK_DEP: bool
    RESCHEDULEABLE_STATES: Incomplete
