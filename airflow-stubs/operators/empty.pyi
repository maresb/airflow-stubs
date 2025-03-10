import airflow.models.baseoperator
from airflow.models.baseoperator import BaseOperator as BaseOperator
from typing import ClassVar

TYPE_CHECKING: bool

class EmptyOperator(airflow.models.baseoperator.BaseOperator):
    ui_color: ClassVar[str] = ...
    inherits_from_empty_operator: ClassVar[bool] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def execute(self, context: Context): ...
    def __init__(self, *args, **kwargs) -> None: ...
