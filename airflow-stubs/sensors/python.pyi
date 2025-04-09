from _typeshed import Incomplete
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator, PokeReturnValue as PokeReturnValue
from airflow.utils.context import Context as Context, context_merge as context_merge
from airflow.utils.operator_helpers import determine_kwargs as determine_kwargs
from typing import Any, Callable, Mapping, Sequence

class PythonSensor(BaseSensorOperator):
    template_fields: Sequence[str]
    python_callable: Incomplete
    op_args: Incomplete
    op_kwargs: Incomplete
    templates_dict: Incomplete
    def __init__(self, *, python_callable: Callable, op_args: list | None = None, op_kwargs: Mapping[str, Any] | None = None, templates_dict: dict | None = None, **kwargs) -> None: ...
    def poke(self, context: Context) -> PokeReturnValue | bool: ...
