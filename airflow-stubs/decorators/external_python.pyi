from _typeshed import Incomplete
from airflow.decorators.base import TaskDecorator as TaskDecorator, task_decorator_factory as task_decorator_factory
from airflow.decorators.python import _PythonDecoratedOperator
from airflow.operators.python import ExternalPythonOperator as ExternalPythonOperator
from typing import Callable

class _PythonExternalDecoratedOperator(_PythonDecoratedOperator, ExternalPythonOperator):
    template_fields: Incomplete
    custom_operator_name: str

def external_python_task(python: str | None = None, python_callable: Callable | None = None, multiple_outputs: bool | None = None, **kwargs) -> TaskDecorator: ...
