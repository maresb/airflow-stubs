from _typeshed import Incomplete
from airflow.compat.functools import cache as cache
from airflow.io.typedef import Properties as Properties
from airflow.providers_manager import ProvidersManager as ProvidersManager
from airflow.stats import Stats as Stats
from airflow.utils.module_loading import import_string as import_string
from fsspec import AbstractFileSystem as AbstractFileSystem

log: Incomplete

def get_fs(scheme: str, conn_id: str | None = None, storage_options: Properties | None = None) -> AbstractFileSystem: ...
def has_fs(scheme: str) -> bool: ...
