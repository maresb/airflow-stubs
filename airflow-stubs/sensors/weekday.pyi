import airflow.sensors.base
import airflow.utils.timezone as timezone
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.utils.decorators import warnings as warnings
from airflow.utils.weekday import WeekDay as WeekDay
from typing import ClassVar

TYPE_CHECKING: bool

class DayOfWeekSensor(airflow.sensors.base.BaseSensorOperator):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def poke(self, context: Context) -> bool: ...
