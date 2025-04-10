from airflow.models.taskinstance import PAST_DEPENDS_MET as PAST_DEPENDS_MET
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.db import LazySelectSequence as LazySelectSequence

class NotPreviouslySkippedDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    IS_TASK_DEP: bool
