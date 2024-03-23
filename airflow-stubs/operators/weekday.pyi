import airflow.operators.branch
import airflow.utils.timezone as timezone
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.operators.branch import BaseBranchOperator as BaseBranchOperator
from airflow.utils.decorators import warnings as warnings
from airflow.utils.weekday import WeekDay as WeekDay
from typing import ClassVar, Iterable

TYPE_CHECKING: bool

class BranchDayOfWeekOperator(airflow.operators.branch.BaseBranchOperator):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def choose_branch(self, context: Context) -> str | Iterable[str]: ...
