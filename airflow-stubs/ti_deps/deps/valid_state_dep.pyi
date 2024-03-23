import airflow.ti_deps.deps.base_ti_dep
from airflow.exceptions import AirflowException as AirflowException
from airflow.ti_deps.deps.base_ti_dep import BaseTIDep as BaseTIDep
from airflow.utils.session import provide_session as provide_session
from typing import ClassVar

class ValidStateDep(airflow.ti_deps.deps.base_ti_dep.BaseTIDep):
    NAME: ClassVar[str] = ...
    IGNORABLE: ClassVar[bool] = ...
    def __init__(self, valid_states) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
