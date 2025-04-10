from _typeshed import Incomplete
from airflow.exceptions import AirflowException as AirflowException, AirflowNotFoundException as AirflowNotFoundException
from airflow.hooks.base import BaseHook as BaseHook
from airflow.models import Connection as Connection
from docker import APIClient, TLSConfig
from functools import cached_property as cached_property
from typing import Any

class DockerHook(BaseHook):
    conn_name_attr: str
    default_conn_name: str
    conn_type: str
    hook_name: str
    docker_conn_id: Incomplete
    def __init__(self, docker_conn_id: str | None = ..., base_url: str | list[str] | None = None, version: str | None = None, tls: TLSConfig | bool | None = None, timeout: int = ...) -> None: ...
    @staticmethod
    def construct_tls_config(ca_cert: str | None = None, client_cert: str | None = None, client_key: str | None = None, verify: bool = True, assert_hostname: str | bool | None = None, ssl_version: str | None = None) -> TLSConfig | bool: ...
    @cached_property
    def api_client(self) -> APIClient: ...
    @property
    def client_created(self) -> bool: ...
    def get_conn(self) -> APIClient: ...
    @classmethod
    def get_connection_form_widgets(cls) -> dict[str, Any]: ...
    @classmethod
    def get_ui_field_behaviour(cls) -> dict[str, Any]: ...
