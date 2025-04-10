from _typeshed import Incomplete
from airflow.decorators.base import DecoratedOperator as DecoratedOperator, TaskDecorator as TaskDecorator, task_decorator_factory as task_decorator_factory
from airflow.exceptions import AirflowException as AirflowException
from airflow.providers.common.compat.standard.utils import write_python_script as write_python_script
from airflow.providers.docker.operators.docker import DockerOperator as DockerOperator
from airflow.utils.context import Context as Context
from collections.abc import Sequence
from typing import Callable

Serializer: Incomplete
log: Incomplete

class _DockerDecoratedOperator(DecoratedOperator, DockerOperator):
    custom_operator_name: str
    template_fields: Sequence[str]
    python_command: Incomplete
    expect_airflow: Incomplete
    serializer: Serializer
    def __init__(self, python_command: str = 'python3', expect_airflow: bool = True, serializer: Serializer | None = None, **kwargs) -> None: ...
    def generate_command(self): ...
    command: Incomplete
    def execute(self, context: Context): ...
    @property
    def pickling_library(self): ...

def docker_task(python_callable: Callable | None = None, multiple_outputs: bool | None = None, **kwargs) -> TaskDecorator: ...
