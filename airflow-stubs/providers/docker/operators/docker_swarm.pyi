from _typeshed import Incomplete
from airflow.exceptions import AirflowException as AirflowException
from airflow.providers.docker.operators.docker import DockerOperator as DockerOperator
from airflow.utils.context import Context as Context
from airflow.utils.strings import get_random_string as get_random_string
from docker import types
from typing import Literal

class DockerSwarmOperator(DockerOperator):
    args: Incomplete
    enable_logging: Incomplete
    service: Incomplete
    tasks: list[dict]
    containers: list[dict]
    configs: Incomplete
    secrets: Incomplete
    mode: Incomplete
    networks: Incomplete
    placement: Incomplete
    container_resources: Incomplete
    logging_driver: Incomplete
    logging_driver_opts: Incomplete
    log_driver_config: Incomplete
    def __init__(self, *, image: str, args: str | list[str] | None = None, enable_logging: bool = True, configs: list[types.ConfigReference] | None = None, secrets: list[types.SecretReference] | None = None, mode: types.ServiceMode | None = None, networks: list[str | types.NetworkAttachmentConfig] | None = None, placement: types.Placement | list[types.Placement] | None = None, container_resources: types.Resources | None = None, logging_driver: Literal['json-path', 'gelf'] | None = None, logging_driver_opts: dict | None = None, **kwargs) -> None: ...
    def execute(self, context: Context) -> None: ...
    @staticmethod
    def format_args(args: list[str] | str | None) -> list[str] | None: ...
    def on_kill(self) -> None: ...
