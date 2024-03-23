import airflow.decorators.base
import airflow.operators.python
from airflow.decorators.base import DecoratedOperator as DecoratedOperator, task_decorator_factory as task_decorator_factory
from airflow.operators.python import PythonOperator as PythonOperator
from typing import Callable, ClassVar

TYPE_CHECKING: bool

class _PythonDecoratedOperator(airflow.decorators.base.DecoratedOperator, airflow.operators.python.PythonOperator):
    template_fields: ClassVar[tuple] = ...
    template_fields_renderers: ClassVar[dict] = ...
    custom_operator_name: ClassVar[str] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
def python_task(python_callable: Callable | None = ..., multiple_outputs: bool | None = ..., **kwargs) -> TaskDecorator: ...