import logging
from _typeshed import Incomplete
from airflow.utils.helpers import merge_dicts as merge_dicts

class JSONFormatter(logging.Formatter):
    json_fields: Incomplete
    extras: Incomplete
    def __init__(self, fmt: Incomplete | None = None, datefmt: Incomplete | None = None, style: str = '%', json_fields: Incomplete | None = None, extras: Incomplete | None = None) -> None: ...
    def usesTime(self): ...
    def format(self, record): ...
