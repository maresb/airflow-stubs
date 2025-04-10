from _typeshed import Incomplete
from airflow.exceptions import AirflowException as AirflowException, AirflowSkipException as AirflowSkipException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.hooks.subprocess import SubprocessHook as SubprocessHook, SubprocessResult as SubprocessResult, working_directory as working_directory
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils.context import Context as Context
from airflow.utils.operator_helpers import context_to_airflow_vars as context_to_airflow_vars
from airflow.utils.types import ArgNotSet as ArgNotSet
from functools import cached_property as cached_property
from typing import Any, Callable, Container, Sequence

class BashOperator(BaseOperator):
    template_fields: Sequence[str]
    template_fields_renderers: Incomplete
    template_ext: Sequence[str]
    ui_color: str
    bash_command: Incomplete
    env: Incomplete
    output_encoding: Incomplete
    skip_on_exit_code: Incomplete
    cwd: Incomplete
    append_env: Incomplete
    output_processor: Incomplete
    def __init__(self, *, bash_command: str | ArgNotSet, env: dict[str, str] | None = None, append_env: bool = False, output_encoding: str = 'utf-8', skip_exit_code: int | None = None, skip_on_exit_code: int | Container[int] | None = 99, cwd: str | None = None, output_processor: Callable[[str], Any] = ..., **kwargs) -> None: ...
    @cached_property
    def subprocess_hook(self): ...
    @staticmethod
    def refresh_bash_command(ti: TaskInstance) -> None: ...
    def get_env(self, context) -> dict: ...
    def execute(self, context: Context): ...
    def on_kill(self) -> None: ...
