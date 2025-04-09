from _typeshed import Incomplete
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.connection import Connection as Connection
from airflow.typing_compat import Protocol as Protocol
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

log: Incomplete

class BaseHook(LoggingMixin):
    def __init__(self, logger_name: str | None = None) -> None: ...
    @classmethod
    def get_connections(cls, conn_id: str) -> list[Connection]: ...
    @classmethod
    def get_connection(cls, conn_id: str) -> Connection: ...
    @classmethod
    def get_hook(cls, conn_id: str) -> BaseHook: ...
    def get_conn(self) -> Any: ...
    @classmethod
    def get_connection_form_widgets(cls) -> dict[str, Any]: ...
    @classmethod
    def get_ui_field_behaviour(cls) -> dict[str, Any]: ...

class DiscoverableHook(Protocol):
    conn_name_attr: str
    default_conn_name: str
    conn_type: str
    hook_name: str
    @staticmethod
    def get_connection_form_widgets() -> dict[str, Any]: ...
    @staticmethod
    def get_ui_field_behaviour() -> dict[str, Any]: ...
