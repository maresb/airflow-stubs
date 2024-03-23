import typing
from . import backend as backend
from airflow.configuration import conf as conf
from airflow.lineage.backend import LineageBackend as LineageBackend
from airflow.utils.session import create_session as create_session

TYPE_CHECKING: bool
PIPELINE_OUTLETS: str
PIPELINE_INLETS: str
AUTO: str
def get_backend() -> LineageBackend | None: ...

T: typing.TypeVar
def apply_lineage(func: T) -> T: ...
def prepare_lineage(func: T) -> T: ...
