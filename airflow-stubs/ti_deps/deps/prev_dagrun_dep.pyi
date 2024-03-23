import airflow.ti_deps.deps.base_ti_dep
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.taskinstance import TI as TI
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.db import exists_query as exists_query
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from typing import ClassVar

TYPE_CHECKING: bool
PAST_DEPENDS_MET: str

class PrevDagrunDep(airflow.ti_deps.deps.base_ti_dep.BaseTIDep):
    NAME: ClassVar[str] = ...
    IGNORABLE: ClassVar[bool] = ...
    IS_TASK_DEP: ClassVar[bool] = ...
