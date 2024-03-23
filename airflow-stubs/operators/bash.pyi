import airflow.models.baseoperator
import functools
from airflow.exceptions import AirflowException as AirflowException, AirflowSkipException as AirflowSkipException
from airflow.hooks.subprocess import SubprocessHook as SubprocessHook
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.utils.decorators import warnings as warnings
from airflow.utils.operator_helpers import context_to_airflow_vars as context_to_airflow_vars
from typing import ClassVar

TYPE_CHECKING: bool

class BashOperator(airflow.models.baseoperator.BaseOperator):
    template_fields: ClassVar[tuple] = ...
    template_fields_renderers: ClassVar[dict] = ...
    template_ext: ClassVar[tuple] = ...
    ui_color: ClassVar[str] = ...
    subprocess_hook: ClassVar[functools.cached_property] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def get_env(self, context): ...
    def execute(self, context: Context): ...
    def on_kill(self) -> None: ...
