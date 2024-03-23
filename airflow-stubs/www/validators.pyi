import airflow.utils.helpers as helpers
import wtforms.validators
from _typeshed import Incomplete
from airflow.models.connection import sanitize_conn_id as sanitize_conn_id
from typing import ClassVar

CONN_ID_MAX_LEN: int

class GreaterEqualThan(wtforms.validators.EqualTo):
    def __call__(self, form, field): ...

class ValidJson:
    def __init__(self, message: Incomplete | None = ...) -> None: ...
    def __call__(self, form, field): ...

class ValidKey:
    def __init__(self, max_length: int = ...) -> None: ...
    def __call__(self, form, field): ...

class ReadOnly:
    def __call__(self, form, field): ...

class ValidConnID:
    message: ClassVar[str] = ...
    def __init__(self, max_length: int = ...) -> None: ...
    def __call__(self, form, field): ...
