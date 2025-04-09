from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.hooks.filesystem import FSHook as FSHook
from airflow.sensors.base import BaseSensorOperator as BaseSensorOperator
from airflow.triggers.base import StartTriggerArgs as StartTriggerArgs
from airflow.triggers.file import FileTrigger as FileTrigger
from airflow.utils.context import Context as Context
from functools import cached_property as cached_property
from typing import Any, Sequence

class FileSensor(BaseSensorOperator):
    template_fields: Sequence[str]
    ui_color: str
    start_trigger_args: Incomplete
    start_from_trigger: bool
    filepath: Incomplete
    fs_conn_id: Incomplete
    recursive: Incomplete
    deferrable: Incomplete
    def __init__(self, *, filepath, fs_conn_id: str = 'fs_default', recursive: bool = False, deferrable: bool = ..., start_from_trigger: bool = False, trigger_kwargs: dict[str, Any] | None = None, **kwargs) -> None: ...
    @cached_property
    def path(self) -> str: ...
    def poke(self, context: Context) -> bool: ...
    def execute(self, context: Context) -> None: ...
    def execute_complete(self, context: Context, event: bool | None = None) -> None: ...
