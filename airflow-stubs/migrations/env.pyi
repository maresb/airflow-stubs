from _typeshed import Incomplete
from airflow import models as models, settings as settings
from airflow.utils.db import compare_server_default as compare_server_default, compare_type as compare_type
from airflow.www.app import purge_cached_app as purge_cached_app

def include_object(_, name, type_, *args): ...

config: Incomplete
target_metadata: Incomplete

def run_migrations_offline() -> None: ...
def run_migrations_online() -> None: ...
