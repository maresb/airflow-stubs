from _typeshed import Incomplete
from airflow.decorators.base import TaskDecorator as TaskDecorator, task_decorator_factory as task_decorator_factory
from airflow.decorators.python import _PythonDecoratedOperator
from airflow.operators.python import BranchPythonOperator as BranchPythonOperator
from typing import Callable

class _BranchPythonDecoratedOperator(_PythonDecoratedOperator, BranchPythonOperator):
    template_fields: Incomplete
    custom_operator_name: str

def branch_task(python_callable: Callable | None = None, multiple_outputs: bool | None = None, **kwargs) -> TaskDecorator: ...
