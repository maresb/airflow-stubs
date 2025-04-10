from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models.connection import Connection as Connection
from airflow.secrets import BaseSecretsBackend as BaseSecretsBackend
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from sqlalchemy.orm import Session as Session

class MetastoreBackend(BaseSecretsBackend):
    def get_connection(self, conn_id: str, session: Session = ...) -> Connection | None: ...
    def get_connections(self, conn_id: str, session: Session = ...) -> list[Connection]: ...
    def get_variable(self, key: str, session: Session = ...) -> str | None: ...
