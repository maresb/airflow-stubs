import airflow.secrets.base_secrets
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.secrets.base_secrets import BaseSecretsBackend as BaseSecretsBackend
from typing import ClassVar

CONN_ENV_PREFIX: str
VAR_ENV_PREFIX: str

class EnvironmentVariablesBackend(airflow.secrets.base_secrets.BaseSecretsBackend):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def get_conn_uri(self, conn_id: str) -> str | None: ...
    def get_conn_value(self, conn_id: str) -> str | None: ...
    def get_variable(self, key: str) -> str | None: ...
