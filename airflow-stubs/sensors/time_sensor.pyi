import datetime
from _typeshed import Incomplete
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.triggers.base import StartTriggerArgs as StartTriggerArgs
from airflow.triggers.temporal import DateTimeTrigger as DateTimeTrigger
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context
from typing import Any, NoReturn

class TimeSensor(BaseSensorOperator):
    target_time: Incomplete
    def __init__(self, *, target_time: datetime.time, **kwargs) -> None: ...
    def poke(self, context: Context) -> bool: ...

class TimeSensorAsync(BaseSensorOperator):
    start_trigger_args: Incomplete
    start_from_trigger: bool
    end_from_trigger: Incomplete
    target_time: Incomplete
    target_datetime: Incomplete
    def __init__(self, *, target_time: datetime.time, start_from_trigger: bool = False, trigger_kwargs: dict[str, Any] | None = None, end_from_trigger: bool = False, **kwargs) -> None: ...
    def execute(self, context: Context) -> NoReturn: ...
    def execute_complete(self, context: Context, event: Any = None) -> None: ...
