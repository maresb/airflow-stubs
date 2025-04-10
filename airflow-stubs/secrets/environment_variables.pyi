from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.secrets import BaseSecretsBackend as BaseSecretsBackend

CONN_ENV_PREFIX: str
VAR_ENV_PREFIX: str

class EnvironmentVariablesBackend(BaseSecretsBackend):
    def get_conn_uri(self, conn_id: str) -> str | None: ...
    def get_conn_value(self, conn_id: str) -> str | None: ...
    def get_variable(self, key: str) -> str | None: ...
