from _typeshed import Incomplete
from airflow.auth.managers.models.base_user import BaseUser as BaseUser
from airflow.configuration import conf as conf
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.utils.airflow_flask_app import get_airflow_app as get_airflow_app
from airflow.utils.net import getfqdn as getfqdn
from typing import Callable, NamedTuple, TypeVar

log: Incomplete

class KerberosService:
    service_name: Incomplete
    def __init__(self) -> None: ...

class _KerberosAuth(NamedTuple):
    return_code: int | None
    user: str = ...
    token: str | None = ...

def init_app(app) -> None: ...
T = TypeVar('T', bound=Callable)

def requires_authentication(function: T, find_user: Callable[[str], BaseUser] | None = None): ...
def __getattr__(name): ...
