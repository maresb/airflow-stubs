import airflow.hooks.base
from airflow.hooks.base import BaseHook as BaseHook
from typing import Any, ClassVar

class FSHook(airflow.hooks.base.BaseHook):
    conn_name_attr: ClassVar[str] = ...
    default_conn_name: ClassVar[str] = ...
    conn_type: ClassVar[str] = ...
    hook_name: ClassVar[str] = ...
    @classmethod
    def get_connection_form_widgets(cls) -> dict[str, Any]: ...
    @classmethod
    def get_ui_field_behaviour(cls) -> dict[str, Any]: ...
    def __init__(self, fs_conn_id: str = ..., **kwargs) -> None: ...
    def get_conn(self) -> None: ...
    def get_path(self) -> str: ...
    def test_connection(self): ...
