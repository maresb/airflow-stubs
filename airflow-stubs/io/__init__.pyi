from . import path as path, store as store, utils as utils
from airflow.providers_manager import ProvidersManager as ProvidersManager
from airflow.stats import Stats as Stats
from airflow.utils.module_loading import import_string as import_string

TYPE_CHECKING: bool
def get_fs(scheme: str, conn_id: str | None = ..., storage_options: Properties | None = ...) -> AbstractFileSystem: ...
def has_fs(scheme: str) -> bool: ...
