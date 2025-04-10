from _typeshed import Incomplete
from airflow.decorators.base import DecoratedOperator as DecoratedOperator, TaskDecorator as TaskDecorator, task_decorator_factory as task_decorator_factory
from airflow.operators.python import PythonOperator as PythonOperator
from typing import Callable, Sequence

class _PythonDecoratedOperator(DecoratedOperator, PythonOperator):
    template_fields: Sequence[str]
    template_fields_renderers: Incomplete
    custom_operator_name: str
    def __init__(self, *, python_callable, op_args, op_kwargs, **kwargs) -> None: ...

def python_task(python_callable: Callable | None = None, multiple_outputs: bool | None = None, **kwargs) -> TaskDecorator: ...
