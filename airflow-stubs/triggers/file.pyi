import airflow.triggers.base
import typing
from airflow.triggers.base import BaseTrigger as BaseTrigger, TriggerEvent as TriggerEvent
from typing import Any, ClassVar

class FileTrigger(airflow.triggers.base.BaseTrigger):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, filepath: str, recursive: bool = ..., poll_interval: float = ...) -> None: ...
    def serialize(self) -> tuple[str, dict[str, Any]]: ...
    def run(self) -> typing.AsyncIterator[TriggerEvent]: ...
