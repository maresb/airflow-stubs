from _typeshed import Incomplete
from airflow.models import BaseOperator as BaseOperator
from airflow.providers.docker.exceptions import DockerContainerFailedException as DockerContainerFailedException, DockerContainerFailedSkipException as DockerContainerFailedSkipException
from airflow.providers.docker.hooks.docker import DockerHook as DockerHook
from airflow.utils.context import Context as Context
from collections.abc import Container, Iterable, Sequence
from docker import APIClient as APIClient
from docker.types import DeviceRequest as DeviceRequest, Mount, Ulimit as Ulimit
from functools import cached_property as cached_property
from logging import Logger
from typing_extensions import Literal

def stringify(line: str | bytes): ...
def fetch_logs(log_stream, log: Logger): ...

class DockerOperator(BaseOperator):
    template_fields: Sequence[str]
    template_fields_renderers: Incomplete
    template_ext: Sequence[str]
    api_version: Incomplete
    auto_remove: Incomplete
    command: Incomplete
    container_name: Incomplete
    cpus: Incomplete
    dns: Incomplete
    dns_search: Incomplete
    docker_url: Incomplete
    environment: Incomplete
    env_file: Incomplete
    force_pull: Incomplete
    image: Incomplete
    mem_limit: Incomplete
    host_tmp_dir: Incomplete
    network_mode: Incomplete
    tls_ca_cert: Incomplete
    tls_client_cert: Incomplete
    tls_client_key: Incomplete
    tls_verify: Incomplete
    tls_hostname: Incomplete
    tls_ssl_version: Incomplete
    mount_tmp_dir: Incomplete
    tmp_dir: Incomplete
    user: Incomplete
    mounts: Incomplete
    entrypoint: Incomplete
    working_dir: Incomplete
    xcom_all: Incomplete
    docker_conn_id: Incomplete
    shm_size: Incomplete
    tty: Incomplete
    hostname: Incomplete
    privileged: Incomplete
    cap_add: Incomplete
    extra_hosts: Incomplete
    ulimits: Incomplete
    container: dict
    retrieve_output: Incomplete
    retrieve_output_path: Incomplete
    timeout: Incomplete
    device_requests: Incomplete
    log_opts_max_size: Incomplete
    log_opts_max_file: Incomplete
    ipc_mode: Incomplete
    skip_on_exit_code: Incomplete
    port_bindings: Incomplete
    def __init__(self, *, image: str, api_version: str | None = None, command: str | list[str] | None = None, container_name: str | None = None, cpus: float = 1.0, docker_url: str | list[str] | None = None, environment: dict | None = None, private_environment: dict | None = None, env_file: str | None = None, force_pull: bool = False, mem_limit: float | str | None = None, host_tmp_dir: str | None = None, network_mode: str | None = None, tls_ca_cert: str | None = None, tls_client_cert: str | None = None, tls_client_key: str | None = None, tls_verify: bool = True, tls_hostname: str | bool | None = None, tls_ssl_version: str | None = None, mount_tmp_dir: bool = True, tmp_dir: str = '/tmp/airflow', user: str | int | None = None, mounts: list[Mount] | None = None, entrypoint: str | list[str] | None = None, working_dir: str | None = None, xcom_all: bool = False, docker_conn_id: str | None = None, dns: list[str] | None = None, dns_search: list[str] | None = None, auto_remove: Literal['never', 'success', 'force'] = 'never', shm_size: int | None = None, tty: bool = False, hostname: str | None = None, privileged: bool = False, cap_add: Iterable[str] | None = None, extra_hosts: dict[str, str] | None = None, retrieve_output: bool = False, retrieve_output_path: str | None = None, timeout: int = ..., device_requests: list[DeviceRequest] | None = None, log_opts_max_size: str | None = None, log_opts_max_file: str | None = None, ipc_mode: str | None = None, skip_on_exit_code: int | Container[int] | None = None, port_bindings: dict | None = None, ulimits: list[Ulimit] | None = None, **kwargs) -> None: ...
    @cached_property
    def hook(self) -> DockerHook: ...
    @property
    def cli(self) -> APIClient: ...
    def execute(self, context: Context) -> list[str] | str | None: ...
    @staticmethod
    def format_command(command: list[str] | str | None) -> list[str] | str | None: ...
    def on_kill(self) -> None: ...
    @staticmethod
    def unpack_environment_variables(env_str: str) -> dict: ...
