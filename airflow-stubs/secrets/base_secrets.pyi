import abc
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from typing import ClassVar

TYPE_CHECKING: bool

class BaseSecretsBackend(abc.ABC):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    @staticmethod
    def build_path(path_prefix: str, secret_id: str, sep: str = ...) -> str: ...
    def get_conn_value(self, conn_id: str) -> str | None: ...
    def deserialize_connection(self, conn_id: str, value: str) -> Connection: ...
    def get_conn_uri(self, conn_id: str) -> str | None: ...
    def get_connection(self, conn_id: str) -> Connection | None: ...
    def get_connections(self, conn_id: str) -> list[Connection]: ...
    def get_variable(self, key: str) -> str | None: ...
    def get_config(self, key: str) -> str | None: ...
