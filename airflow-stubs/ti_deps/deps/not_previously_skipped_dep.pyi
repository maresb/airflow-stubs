import airflow.ti_deps.deps.base_ti_dep
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from typing import ClassVar

PAST_DEPENDS_MET: str

class NotPreviouslySkippedDep(airflow.ti_deps.deps.base_ti_dep.BaseTIDep):
    NAME: ClassVar[str] = ...
    IGNORABLE: ClassVar[bool] = ...
    IS_TASK_DEP: ClassVar[bool] = ...
