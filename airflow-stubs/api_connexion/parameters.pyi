from _typeshed import Incomplete
from airflow.api_connexion.exceptions import BadRequest as BadRequest
from airflow.configuration import conf as conf
from airflow.utils import timezone as timezone
from datetime import datetime
from sqlalchemy.sql import Select as Select
from typing import Any, Callable, Container, TypeVar

log: Incomplete

def validate_istimezone(value: datetime) -> None: ...
def format_datetime(value: str) -> datetime: ...
def check_limit(value: int) -> int: ...
T = TypeVar('T', bound=Callable)

def format_parameters(params_formatters: dict[str, Callable[[Any], Any]]) -> Callable[[T], T]: ...
def apply_sorting(query: Select, order_by: str, to_replace: dict[str, str] | None = None, allowed_attrs: Container[str] | None = None) -> Select: ...
