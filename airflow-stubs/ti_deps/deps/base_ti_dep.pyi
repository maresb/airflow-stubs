from _typeshed import Incomplete
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.utils.session import provide_session as provide_session
from typing import Any, ClassVar, Iterator

TYPE_CHECKING: bool

class BaseTIDep:
    IGNORABLE: ClassVar[bool] = ...
    IS_TASK_DEP: ClassVar[bool] = ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def get_dep_statuses(self, *args, **kwargs) -> Iterator[TIDepStatus]: ...
    def is_met(self, *args, **kwargs) -> bool: ...
    def get_failure_reasons(self, *args, **kwargs) -> Iterator[str]: ...
    @property
    def name(self): ...

class TIDepStatus(tuple):
    _fields: ClassVar[tuple] = ...
    _field_defaults: ClassVar[dict] = ...
    _fields_defaults: ClassVar[dict] = ...
    _field_types: ClassVar[dict] = ...
    dep_name: Incomplete
    passed: Incomplete
    reason: Incomplete
    def __init__(self, _cls, dep_name: str, passed: bool, reason: str) -> None: ...
    def __getnewargs__(self): ...