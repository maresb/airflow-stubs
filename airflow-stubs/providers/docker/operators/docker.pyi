import airflow.models.baseoperator
import functools
from airflow.exceptions import AirflowProviderDeprecationWarning as AirflowProviderDeprecationWarning
from airflow.models.baseoperator import BaseOperator as BaseOperator
from airflow.providers.docker.exceptions import DockerContainerFailedException as DockerContainerFailedException, DockerContainerFailedSkipException as DockerContainerFailedSkipException
from airflow.providers.docker.hooks.docker import DockerHook as DockerHook
from airflow.utils.decorators import warnings as warnings
from typing import ClassVar

TYPE_CHECKING: bool
DEFAULT_TIMEOUT_SECONDS: int
def stringify(line: str | bytes): ...

class DockerOperator(airflow.models.baseoperator.BaseOperator):
    template_fields: ClassVar[tuple] = ...
    template_fields_renderers: ClassVar[dict] = ...
    template_ext: ClassVar[tuple] = ...
    hook: ClassVar[functools.cached_property] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def get_hook(self) -> DockerHook: ...
    def execute(self, context: Context) -> list[str] | str | None: ...
    @staticmethod
    def format_command(command: list[str] | str | None) -> list[str] | str | None: ...
    def on_kill(self) -> None: ...
    @staticmethod
    def unpack_environment_variables(env_str: str) -> dict: ...
    @property
    def cli(self): ...