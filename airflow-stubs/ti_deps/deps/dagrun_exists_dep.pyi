from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.session import provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState

class DagrunRunningDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
