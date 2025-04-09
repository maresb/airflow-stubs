from _typeshed import Incomplete
from airflow.hooks.base import BaseHook as BaseHook
from typing import Any

class PackageIndexHook(BaseHook):
    conn_name_attr: str
    default_conn_name: str
    conn_type: str
    hook_name: str
    pi_conn_id: Incomplete
    conn: Incomplete
    def __init__(self, pi_conn_id: str = ..., **kwargs) -> None: ...
    @staticmethod
    def get_ui_field_behaviour() -> dict[str, Any]: ...
    def get_conn(self) -> Any: ...
    def get_connection_url(self) -> Any: ...
    def test_connection(self) -> tuple[bool, str]: ...
