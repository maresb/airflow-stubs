import FParams
import airflow.models.baseoperator
import airflow.models.mappedoperator
import airflow.utils.timezone as timezone
import datetime
import functools
import typing
import typing_extensions
from _typeshed import Incomplete
from airflow.datasets import Dataset as Dataset
from airflow.exceptions import AirflowException as AirflowException
from airflow.models.baseoperator import BaseOperator as BaseOperator, coerce_resources as coerce_resources, coerce_timedelta as coerce_timedelta, get_merged_defaults as get_merged_defaults, parse_retries as parse_retries
from airflow.models.dag import DagContext as DagContext
from airflow.models.expandinput import DictOfListsExpandInput as DictOfListsExpandInput, EXPAND_INPUT_EMPTY as EXPAND_INPUT_EMPTY, ListOfDictsExpandInput as ListOfDictsExpandInput, is_mappable as is_mappable
from airflow.models.mappedoperator import MappedOperator as MappedOperator, ensure_xcomarg_return_value as ensure_xcomarg_return_value
from airflow.models.pool import Pool as Pool
from airflow.models.xcom_arg import XComArg as XComArg
from airflow.utils.decorators import remove_task_decorator as remove_task_decorator, warnings as warnings
from airflow.utils.helpers import prevent_duplicates as prevent_duplicates
from airflow.utils.task_group import TaskGroupContext as TaskGroupContext
from airflow.utils.trigger_rule import TriggerRule as TriggerRule
from airflow.utils.types import NOTSET as NOTSET
from typing import Any, Callable, ClassVar as _ClassVar

TYPE_CHECKING: bool
DEFAULT_RETRIES: int
DEFAULT_RETRY_DELAY: datetime.timedelta
KNOWN_CONTEXT_KEYS: set

class ExpandableFactory(typing.Protocol):
    function_signature: _ClassVar[functools.cached_property] = ...
    _mappable_function_argument_names: _ClassVar[functools.cached_property] = ...
    __parameters__: _ClassVar[tuple] = ...
    _is_protocol: _ClassVar[bool] = ...
    __abstractmethods__: _ClassVar[frozenset] = ...
    _abc_impl: _ClassVar[_abc_data] = ...
    def __subclasshook__(self, other): ...
    def __init__(self, *args, **kwargs) -> None: ...
def get_unique_task_id(task_id: str, dag: DAG | None = ..., task_group: TaskGroup | None = ...) -> str: ...

class DecoratedOperator(airflow.models.baseoperator.BaseOperator):
    template_fields: _ClassVar[tuple] = ...
    template_fields_renderers: _ClassVar[dict] = ...
    shallow_copy_attrs: _ClassVar[tuple] = ...
    __abstractmethods__: _ClassVar[frozenset] = ...
    _abc_impl: _ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def execute(self, context: Context): ...
    def get_python_source(self): ...
FParams: typing_extensions.ParamSpec
FReturn: typing.TypeVar
OperatorSubclass: typing.TypeVar

class _TaskDecorator(ExpandableFactory):
    _airflow_is_task_decorator: _ClassVar[bool] = ...
    __orig_bases__: _ClassVar[tuple] = ...
    __parameters__: _ClassVar[tuple] = ...
    _is_protocol: _ClassVar[bool] = ...
    __abstractmethods__: _ClassVar[frozenset] = ...
    _abc_impl: _ClassVar[_abc_data] = ...
    __attrs_attrs__: _ClassVar[_TaskDecoratorAttributes] = ...
    __attrs_own_setattr__: _ClassVar[bool] = ...
    def __attrs_post_init__(self): ...
    def __call__(self, *args: FParams.args, **kwargs: FParams.kwargs) -> XComArg: ...
    def expand(self, **map_kwargs: OperatorExpandArgument) -> XComArg: ...
    def expand_kwargs(self, kwargs: OperatorExpandKwargsArgument) -> XComArg: ...
    def partial(self, **kwargs: Any) -> _TaskDecorator[FParams, FReturn, OperatorSubclass]: ...
    def override(self, **kwargs: Any) -> _TaskDecorator[FParams, FReturn, OperatorSubclass]: ...
    def __subclasshook__(self, other): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __setattr__(self, name, val): ...
    def __init__(self, function: Callable[FParams, FReturn], operator_class: type[OperatorSubclass], multiple_outputs: bool = ..., kwargs: dict[str, Any] = ..., decorator_name: str = ..., is_setup: bool = ..., is_teardown: bool = ..., on_failure_fail_dagrun: bool = ...) -> None: ...
    @property
    def __wrapped__(self): ...

class DecoratedMappedOperator(airflow.models.mappedoperator.MappedOperator):
    __abstractmethods__: _ClassVar[frozenset] = ...
    _abc_impl: _ClassVar[_abc_data] = ...
    __attrs_attrs__: _ClassVar[DecoratedMappedOperatorAttributes] = ...
    __attrs_own_setattr__: _ClassVar[bool] = ...
    multiple_outputs: Incomplete
    op_kwargs_expand_input: Incomplete
    python_callable: Incomplete
    def __hash__(self) -> int: ...
    def __attrs_post_init__(self): ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __init__(self) -> None: ...

class Task(typing.Protocol):
    __orig_bases__: _ClassVar[tuple] = ...
    __parameters__: _ClassVar[tuple] = ...
    _is_protocol: _ClassVar[bool] = ...
    __abstractmethods__: _ClassVar[frozenset] = ...
    _abc_impl: _ClassVar[_abc_data] = ...
    def partial(self, **kwargs: Any) -> Task[FParams, FReturn]: ...
    def expand(self, **kwargs: OperatorExpandArgument) -> XComArg: ...
    def expand_kwargs(self, kwargs: OperatorExpandKwargsArgument) -> XComArg: ...
    def override(self, **kwargs: Any) -> Task[FParams, FReturn]: ...
    def __subclasshook__(self, other): ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def __wrapped__(self): ...

class TaskDecorator(typing.Protocol):
    __parameters__: _ClassVar[tuple] = ...
    _is_protocol: _ClassVar[bool] = ...
    __abstractmethods__: _ClassVar[frozenset] = ...
    _abc_impl: _ClassVar[_abc_data] = ...
    def __call__(self, *args, **kwds): ...
    def override(self, **kwargs: Any) -> Task[FParams, FReturn]: ...
    def __subclasshook__(self, other): ...
    def __init__(self, *args, **kwargs) -> None: ...
def task_decorator_factory(python_callable: Callable | None = ..., **kwargs) -> TaskDecorator: ...