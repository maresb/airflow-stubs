import airflow.sensors.base
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator, PokeReturnValue as PokeReturnValue
from airflow.utils.context import context_merge as context_merge
from airflow.utils.operator_helpers import determine_kwargs as determine_kwargs
from typing import ClassVar

TYPE_CHECKING: bool

class PythonSensor(airflow.sensors.base.BaseSensorOperator):
    template_fields: ClassVar[tuple] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def poke(self, context: Context) -> PokeReturnValue | bool: ...
