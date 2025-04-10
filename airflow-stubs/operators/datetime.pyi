import datetime
from _typeshed import Incomplete
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.operators.branch import BaseBranchOperator as BaseBranchOperator
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context
from typing import Iterable

class BranchDateTimeOperator(BaseBranchOperator):
    target_lower: Incomplete
    target_upper: Incomplete
    follow_task_ids_if_true: Incomplete
    follow_task_ids_if_false: Incomplete
    use_task_logical_date: Incomplete
    def __init__(self, *, follow_task_ids_if_true: str | Iterable[str], follow_task_ids_if_false: str | Iterable[str], target_lower: datetime.datetime | datetime.time | None, target_upper: datetime.datetime | datetime.time | None, use_task_logical_date: bool = False, use_task_execution_date: bool = False, **kwargs) -> None: ...
    def choose_branch(self, context: Context) -> str | Iterable[str]: ...

def target_times_as_dates(base_date: datetime.datetime, lower: datetime.datetime | datetime.time | None, upper: datetime.datetime | datetime.time | None): ...
