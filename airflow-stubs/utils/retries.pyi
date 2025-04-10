import logging
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from typing import Callable, TypeVar, overload

F = TypeVar('F', bound=Callable)
MAX_DB_RETRIES: Incomplete

def run_with_db_retries(max_retries: int = ..., logger: logging.Logger | None = None, **kwargs): ...
@overload
def retry_db_transaction(*, retries: int = ...) -> Callable[[F], F]: ...
@overload
def retry_db_transaction(_func: F) -> F: ...
