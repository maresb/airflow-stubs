from _typeshed import Incomplete
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.operators.branch import BaseBranchOperator as BaseBranchOperator
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context
from airflow.utils.weekday import WeekDay as WeekDay
from typing import Iterable

class BranchDayOfWeekOperator(BaseBranchOperator):
    follow_task_ids_if_true: Incomplete
    follow_task_ids_if_false: Incomplete
    week_day: Incomplete
    use_task_logical_date: Incomplete
    def __init__(self, *, follow_task_ids_if_true: str | Iterable[str], follow_task_ids_if_false: str | Iterable[str], week_day: str | Iterable[str] | WeekDay | Iterable[WeekDay], use_task_logical_date: bool = False, use_task_execution_day: bool = False, **kwargs) -> None: ...
    def choose_branch(self, context: Context) -> str | Iterable[str]: ...
