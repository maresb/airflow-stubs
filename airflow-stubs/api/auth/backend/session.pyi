from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from typing import Any, Callable, TypeVar

CLIENT_AUTH: tuple[str, str] | Any | None

def init_app(_) -> None: ...
T = TypeVar('T', bound=Callable)

def requires_authentication(function: T): ...
