from _typeshed import Incomplete
from airflow import XComArg as XComArg
from airflow.decorators import python_task as python_task
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import BaseOperator as BaseOperator
from airflow.utils.setup_teardown import SetupTeardownContext as SetupTeardownContext
from typing import Callable

def setup_task(func: Callable) -> Callable: ...
def teardown_task(_func: Incomplete | None = None, *, on_failure_fail_dagrun: bool = False) -> Callable: ...

class ContextWrapper(list):
    tasks: Incomplete
    def __init__(self, tasks: list[BaseOperator | XComArg]) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
context_wrapper = ContextWrapper
