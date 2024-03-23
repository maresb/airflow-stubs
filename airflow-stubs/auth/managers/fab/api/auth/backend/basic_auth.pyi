import typing
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app

TYPE_CHECKING: bool
AUTH_LDAP: int
CLIENT_AUTH: None
T: typing.TypeVar
def init_app(_): ...
def auth_current_user() -> User | None: ...
def requires_authentication(function: T): ...
