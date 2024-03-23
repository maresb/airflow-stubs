import airflow.ti_deps.deps.base_ti_dep
import airflow.utils.timezone as timezone
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from typing import ClassVar

class NotInRetryPeriodDep(airflow.ti_deps.deps.base_ti_dep.BaseTIDep):
    NAME: ClassVar[str] = ...
    IGNORABLE: ClassVar[bool] = ...
    IS_TASK_DEP: ClassVar[bool] = ...
