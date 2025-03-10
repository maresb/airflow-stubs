import airflow.models.baseoperator
from airflow.hooks.base import BaseHook as BaseHook
from airflow.models.baseoperator import BaseOperator as BaseOperator
from typing import ClassVar

TYPE_CHECKING: bool

class GenericTransfer(airflow.models.baseoperator.BaseOperator):
    template_fields: ClassVar[tuple] = ...
    template_ext: ClassVar[tuple] = ...
    template_fields_renderers: ClassVar[dict] = ...
    ui_color: ClassVar[str] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def execute(self, context: Context): ...
