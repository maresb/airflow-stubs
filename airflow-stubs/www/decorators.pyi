import airflow.utils.log.secrets_masker as secrets_masker
import typing
from airflow.models.log import Log as Log
from airflow.utils.session import create_session as create_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from typing import Callable

T: typing.TypeVar
def action_logging(func: Callable | None = ..., event: str | None = ...) -> Callable[[T], T]: ...
def gzipped(f: T) -> T: ...
