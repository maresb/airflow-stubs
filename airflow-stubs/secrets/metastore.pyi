import airflow.secrets.base_secrets
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.secrets.base_secrets import BaseSecretsBackend as BaseSecretsBackend
from airflow.utils.session import provide_session as provide_session
from typing import ClassVar

TYPE_CHECKING: bool
NEW_SESSION: None

class MetastoreBackend(airflow.secrets.base_secrets.BaseSecretsBackend):
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def get_connection(self, *args, **kwargs) -> Connection | None: ...
    def get_connections(self, *args, **kwargs) -> list[Connection]: ...
    def get_variable(self, *args, **kwargs) -> str | None: ...
