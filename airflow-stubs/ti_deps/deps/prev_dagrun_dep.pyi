from airflow.models.dagrun import DagRun as DagRun
from airflow.models.operator import Operator as Operator
from airflow.models.taskinstance import PAST_DEPENDS_MET as PAST_DEPENDS_MET
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.db import exists_query as exists_query
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from sqlalchemy.orm import Session as Session

class PrevDagrunDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    IS_TASK_DEP: bool
