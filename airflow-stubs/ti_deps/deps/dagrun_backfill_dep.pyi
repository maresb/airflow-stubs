import airflow.ti_deps.deps.base_ti_dep
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.session import provide_session as provide_session
from airflow.utils.types import DagRunType as DagRunType
from typing import ClassVar

class DagRunNotBackfillDep(airflow.ti_deps.deps.base_ti_dep.BaseTIDep):
    NAME: ClassVar[str] = ...
    IGNORABLE: ClassVar[bool] = ...
