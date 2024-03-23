import logging
import typing
from airflow.configuration import conf as conf
from typing import Callable

F: typing.TypeVar
MAX_DB_RETRIES: int
def run_with_db_retries(max_retries: int = ..., logger: logging.Logger | None = ..., **kwargs): ...
def retry_db_transaction(_func: Callable | None = ..., **retry_kwargs): ...
