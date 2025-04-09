import datetime
from _typeshed import Incomplete
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.triggers.base import StartTriggerArgs as StartTriggerArgs
from airflow.triggers.temporal import DateTimeTrigger as DateTimeTrigger
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context
from typing import Any, NoReturn, Sequence

class DateTimeSensor(BaseSensorOperator):
    template_fields: Sequence[str]
    target_time: Incomplete
    def __init__(self, *, target_time: str | datetime.datetime, **kwargs) -> None: ...
    def poke(self, context: Context) -> bool: ...

class DateTimeSensorAsync(DateTimeSensor):
    start_trigger_args: Incomplete
    start_from_trigger: bool
    end_from_trigger: Incomplete
    def __init__(self, *, start_from_trigger: bool = False, end_from_trigger: bool = False, trigger_kwargs: dict[str, Any] | None = None, **kwargs) -> None: ...
    def execute(self, context: Context) -> NoReturn: ...
    def execute_complete(self, context: Context, event: Any = None) -> None: ...
