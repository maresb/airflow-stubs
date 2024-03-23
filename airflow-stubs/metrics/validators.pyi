from airflow.configuration import conf as conf
from airflow.exceptions import InvalidStatsNameException as InvalidStatsNameException
from typing import Callable, ClassVar, Iterable

class MetricNameLengthExemptionWarning(Warning): ...
ALLOWED_CHARACTERS: frozenset
BACK_COMPAT_METRIC_NAME_PATTERNS: set
BACK_COMPAT_METRIC_NAMES: set
OTEL_NAME_MAX_LENGTH: int
def validate_stat(fn: Callable) -> Callable: ...
def stat_name_otel_handler(stat_prefix: str, stat_name: str, max_length: int = ...) -> str: ...
def stat_name_default_handler(stat_name: str, max_length: int = ..., allowed_chars: Iterable[str] = ...) -> str: ...
def get_current_handler_stat_name_func() -> Callable[[str], str]: ...

class ListValidator:
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, validate_list: str | None = ...) -> None: ...
    @classmethod
    def __subclasshook__(cls, subclass: Callable[[str], str]) -> bool: ...
    def test(self, name: str) -> bool: ...

class AllowListValidator(ListValidator):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def test(self, name: str) -> bool: ...

class BlockListValidator(ListValidator):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def test(self, name: str) -> bool: ...