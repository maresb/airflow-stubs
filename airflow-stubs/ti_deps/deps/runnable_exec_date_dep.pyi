import airflow.ti_deps.deps.base_ti_dep
import airflow.utils.timezone as timezone
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.session import provide_session as provide_session
from typing import ClassVar

class RunnableExecDateDep(airflow.ti_deps.deps.base_ti_dep.BaseTIDep):
    NAME: ClassVar[str] = ...
    IGNORABLE: ClassVar[bool] = ...
