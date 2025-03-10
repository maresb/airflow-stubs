import airflow.decorators.python
import airflow.operators.python
from airflow.decorators.base import task_decorator_factory as task_decorator_factory
from airflow.operators.python import PythonVirtualenvOperator as PythonVirtualenvOperator
from typing import Callable, ClassVar

TYPE_CHECKING: bool

class _PythonVirtualenvDecoratedOperator(airflow.decorators.python._PythonDecoratedOperator, airflow.operators.python.PythonVirtualenvOperator):
    template_fields: ClassVar[tuple] = ...
    custom_operator_name: ClassVar[str] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
def virtualenv_task(python_callable: Callable | None = ..., multiple_outputs: bool | None = ..., **kwargs) -> TaskDecorator: ...
