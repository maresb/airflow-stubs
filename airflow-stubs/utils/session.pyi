import airflow.settings as settings
import typing
import typing_extensions
from sqlalchemy.orm.session import SASession
from typing import Callable, Generator

def create_session(*args, **kwds) -> Generator[SASession, None, None]: ...

PS: typing_extensions.ParamSpec
RT: typing.TypeVar
def find_session_idx(func: Callable[PS, RT]) -> int: ...
def provide_session(func: Callable[PS, RT]) -> Callable[PS, RT]: ...

NEW_SESSION: None
