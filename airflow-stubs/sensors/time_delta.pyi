from _typeshed import Incomplete
from airflow.exceptions import AirflowSkipException as AirflowSkipException
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.triggers.temporal import DateTimeTrigger as DateTimeTrigger
from airflow.utils import timezone as timezone
from airflow.utils.context import Context as Context
from typing import Any, NoReturn

class TimeDeltaSensor(BaseSensorOperator):
    delta: Incomplete
    def __init__(self, *, delta, **kwargs) -> None: ...
    def poke(self, context: Context): ...

class TimeDeltaSensorAsync(TimeDeltaSensor):
    end_from_trigger: Incomplete
    def __init__(self, *, end_from_trigger: bool = False, delta, **kwargs) -> None: ...
    def execute(self, context: Context) -> bool | NoReturn: ...
    def execute_complete(self, context: Context, event: Any = None) -> None: ...
