import typing
from _typeshed import Incomplete
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning

T: typing.TypeVar
def apply_defaults(func: T) -> T: ...
def remove_task_decorator(python_source: str, task_decorator_name: str) -> str: ...

class _autostacklevel_warn:
    def __init__(self) -> None: ...
    def __getattr__(self, name): ...
    def __dir__(self): ...
    def warn(self, message, category: Incomplete | None = ..., stacklevel: int = ..., source: Incomplete | None = ...): ...
def fixup_decorator_warning_stack(func): ...
