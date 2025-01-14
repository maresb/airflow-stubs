import logging
from _typeshed import Incomplete
from airflow.utils.helpers import merge_dicts as merge_dicts

class JSONFormatter(logging.Formatter):
    def __init__(self, fmt: Incomplete | None = ..., datefmt: Incomplete | None = ..., style: str = ..., json_fields: Incomplete | None = ..., extras: Incomplete | None = ...) -> None: ...
    def usesTime(self): ...
    def format(self, record): ...
