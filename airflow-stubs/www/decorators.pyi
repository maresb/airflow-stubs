from _typeshed import Incomplete
from airflow.models import Log as Log
from airflow.utils.log import secrets_masker as secrets_masker
from airflow.utils.session import create_session as create_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from typing import Callable, TypeVar

T = TypeVar('T', bound=Callable)
logger: Incomplete

def action_logging(func: T | None = None, event: str | None = None) -> T | Callable: ...
def gzipped(f: T) -> T: ...
