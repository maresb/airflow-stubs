from airflow.io import get_fs as get_fs, has_fs as has_fs
from airflow.utils.module_loading import qualname as qualname
from typing import ClassVar as _ClassVar

TYPE_CHECKING: bool

class ObjectStore:
    __version__: _ClassVar[int] = ...
    _fs: _ClassVar[None] = ...
    def __init__(self, protocol: str, conn_id: str | None, fs: AbstractFileSystem | None = ..., storage_options: Properties | None = ...) -> None: ...
    def serialize(self): ...
    @classmethod
    def deserialize(cls, data: dict[str, str], version: int): ...
    def __eq__(self, other) -> bool: ...
    @property
    def fs(self): ...
    @property
    def fsid(self): ...
def attach(protocol: str | None = ..., conn_id: str | None = ..., alias: str | None = ..., encryption_type: str | None = ..., fs: AbstractFileSystem | None = ..., **kwargs) -> ObjectStore: ...
