from _typeshed import Incomplete
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context
from airflow.utils.weekday import WeekDay as WeekDay
from typing import Iterable

class DayOfWeekSensor(BaseSensorOperator):
    week_day: Incomplete
    use_task_logical_date: Incomplete
    def __init__(self, *, week_day: str | Iterable[str] | WeekDay | Iterable[WeekDay], use_task_logical_date: bool = False, use_task_execution_day: bool = False, **kwargs) -> None: ...
    def poke(self, context: Context) -> bool: ...
