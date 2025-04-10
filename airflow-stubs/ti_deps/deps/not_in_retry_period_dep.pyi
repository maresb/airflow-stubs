from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils import timezone as timezone
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState

class NotInRetryPeriodDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    IS_TASK_DEP: bool
