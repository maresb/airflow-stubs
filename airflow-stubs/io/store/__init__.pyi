from airflow.io import get_fs as get_fs, has_fs as has_fs
from airflow.io.typedef import Properties as Properties
from airflow.utils.module_loading import qualname as qualname
from fsspec import AbstractFileSystem as AbstractFileSystem
from functools import cached_property as cached_property
from typing import ClassVar

class ObjectStore:
    __version__: ClassVar[int]
    method: str
    conn_id: str | None
    protocol: str
    storage_options: Properties | None
    def __init__(self, protocol: str, conn_id: str | None, fs: AbstractFileSystem | None = None, storage_options: Properties | None = None) -> None: ...
    @cached_property
    def fs(self) -> AbstractFileSystem: ...
    @property
    def fsid(self) -> str: ...
    def serialize(self): ...
    @classmethod
    def deserialize(cls, data: dict[str, str], version: int): ...
    def __eq__(self, other): ...

def attach(protocol: str | None = None, conn_id: str | None = None, alias: str | None = None, encryption_type: str | None = '', fs: AbstractFileSystem | None = None, **kwargs) -> ObjectStore: ...
