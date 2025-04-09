from airflow import settings as settings
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.settings import TracebackSession as TracebackSession, TracebackSessionForTests as TracebackSessionForTests
from airflow.typing_compat import ParamSpec as ParamSpec
from sqlalchemy.orm import Session as SASession
from typing import Callable, Generator, TypeVar

def create_session() -> Generator[SASession, None, None]: ...
PS = ParamSpec('PS')
RT = TypeVar('RT')

def find_session_idx(func: Callable[PS, RT]) -> int: ...
def provide_session(func: Callable[PS, RT]) -> Callable[PS, RT]: ...

NEW_SESSION: SASession
