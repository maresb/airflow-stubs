import airflow.ti_deps.deps.base_ti_dep
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState
from typing import ClassVar

class DagrunRunningDep(airflow.ti_deps.deps.base_ti_dep.BaseTIDep):
    NAME: ClassVar[str] = ...
    IGNORABLE: ClassVar[bool] = ...
