from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.lineage.backend import LineageBackend as LineageBackend
from airflow.utils.context import Context as Context
from airflow.utils.session import create_session as create_session
from typing import Callable, TypeVar

PIPELINE_OUTLETS: str
PIPELINE_INLETS: str
AUTO: str
log: Incomplete

def get_backend() -> LineageBackend | None: ...
T = TypeVar('T', bound=Callable)

def apply_lineage(func: T) -> T: ...
def prepare_lineage(func: T) -> T: ...
