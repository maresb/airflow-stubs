import typing
from _typeshed import Incomplete
from airflow.triggers.base import BaseTrigger as BaseTrigger, TriggerEvent as TriggerEvent
from typing import Any

class FileTrigger(BaseTrigger):
    filepath: Incomplete
    recursive: Incomplete
    poke_interval: float
    def __init__(self, filepath: str, recursive: bool = False, poke_interval: float = 5.0, **kwargs) -> None: ...
    def serialize(self) -> tuple[str, dict[str, Any]]: ...
    async def run(self) -> typing.AsyncIterator[TriggerEvent]: ...
