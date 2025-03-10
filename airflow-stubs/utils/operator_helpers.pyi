import airflow.settings as settings
import typing
from airflow.utils.context import Context as Context, lazy_mapping_from_context as lazy_mapping_from_context
from typing import Any, Callable, Collection, Mapping

R: typing.TypeVar
DEFAULT_FORMAT_PREFIX: str
ENV_VAR_FORMAT_PREFIX: str
AIRFLOW_VAR_NAME_FORMAT_MAPPING: dict
def context_to_airflow_vars(context: Mapping[str, Any], in_env_var_format: bool = ...) -> dict[str, str]: ...

class KeywordParameters:
    def __init__(self, kwargs: Mapping[str, Any]) -> None: ...
    @classmethod
    def determine(cls, func: Callable[..., Any], args: Collection[Any], kwargs: Mapping[str, Any]) -> KeywordParameters: ...
    def unpacking(self) -> Mapping[str, Any]: ...
    def serializing(self) -> Mapping[str, Any]: ...
def determine_kwargs(func: Callable[..., Any], args: Collection[Any], kwargs: Mapping[str, Any]) -> Mapping[str, Any]: ...
def make_kwargs_callable(func: Callable[..., R]) -> Callable[..., R]: ...
