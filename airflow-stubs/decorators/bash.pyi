from _typeshed import Incomplete
from airflow.decorators.base import DecoratedOperator as DecoratedOperator, TaskDecorator as TaskDecorator, task_decorator_factory as task_decorator_factory
from airflow.operators.bash import BashOperator as BashOperator
from airflow.utils.context import Context as Context, context_merge as context_merge
from airflow.utils.operator_helpers import determine_kwargs as determine_kwargs
from airflow.utils.types import NOTSET as NOTSET
from typing import Any, Callable, Collection, Mapping, Sequence

class _BashDecoratedOperator(DecoratedOperator, BashOperator):
    template_fields: Sequence[str]
    template_fields_renderers: dict[str, str]
    custom_operator_name: str
    def __init__(self, *, python_callable: Callable, op_args: Collection[Any] | None = None, op_kwargs: Mapping[str, Any] | None = None, **kwargs) -> None: ...
    bash_command: Incomplete
    def execute(self, context: Context) -> Any: ...

def bash_task(python_callable: Callable | None = None, **kwargs) -> TaskDecorator: ...
