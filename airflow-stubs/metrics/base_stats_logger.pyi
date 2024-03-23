import typing
from airflow.metrics.protocols import Timer as Timer
from typing import ClassVar

TYPE_CHECKING: bool

class StatsLogger(typing.Protocol):
    instance: ClassVar[None] = ...
    __parameters__: ClassVar[tuple] = ...
    _is_protocol: ClassVar[bool] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    @classmethod
    def incr(cls, stat: str, count: int = ..., rate: int | float = ...) -> None: ...
    @classmethod
    def decr(cls, stat: str, count: int = ..., rate: int | float = ...) -> None: ...
    @classmethod
    def gauge(cls, stat: str, value: float, rate: int | float = ..., delta: bool = ...) -> None: ...
    @classmethod
    def timing(cls, stat: str, dt: DeltaType | None) -> None: ...
    @classmethod
    def timer(cls, *args, **kwargs) -> TimerProtocol: ...
    def __subclasshook__(self, other): ...
    def __init__(self, *args, **kwargs) -> None: ...

class NoStatsLogger:
    @classmethod
    def incr(cls, stat: str, count: int = ..., rate: int = ...) -> None: ...
    @classmethod
    def decr(cls, stat: str, count: int = ..., rate: int = ...) -> None: ...
    @classmethod
    def gauge(cls, stat: str, value: int, rate: int = ..., delta: bool = ...) -> None: ...
    @classmethod
    def timing(cls, stat: str, dt: DeltaType) -> None: ...
    @classmethod
    def timer(cls, *args, **kwargs) -> TimerProtocol: ...