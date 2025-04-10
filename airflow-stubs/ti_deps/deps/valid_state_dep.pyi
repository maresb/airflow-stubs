from airflow.exceptions import AirflowException as AirflowException
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.session import provide_session as provide_session

class ValidStateDep(BaseTIDep):
    NAME: str
    IGNORABLE: bool
    def __init__(self, valid_states) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
