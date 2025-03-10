import os
import typing
import zipfile
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from pathlib import Path
from typing import ClassVar, Generator, Pattern

MODIFIED_DAG_MODULE_NAME: str

class _IgnoreRule(typing.Protocol):
    __parameters__: ClassVar[tuple] = ...
    _is_protocol: ClassVar[bool] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    @staticmethod
    def compile(pattern: str, base_dir: Path, definition_file: Path) -> _IgnoreRule | None: ...
    @staticmethod
    def match(path: Path, rules: list[_IgnoreRule]) -> bool: ...
    def __subclasshook__(self, other): ...
    def __init__(self, *args, **kwargs) -> None: ...

class _RegexpIgnoreRule(tuple):
    _fields: ClassVar[tuple] = ...
    _field_defaults: ClassVar[dict] = ...
    _fields_defaults: ClassVar[dict] = ...
    _field_types: ClassVar[dict] = ...
    pattern: Incomplete
    base_dir: Incomplete
    def __init__(self, _cls, pattern: Pattern, base_dir: Path) -> None: ...
    def __getnewargs__(self): ...
    @staticmethod
    def compile(pattern: str, base_dir: Path, definition_file: Path) -> _IgnoreRule | None: ...
    @staticmethod
    def match(path: Path, rules: list[_IgnoreRule]) -> bool: ...

class _GlobIgnoreRule(tuple):
    _fields: ClassVar[tuple] = ...
    _field_defaults: ClassVar[dict] = ...
    _fields_defaults: ClassVar[dict] = ...
    _field_types: ClassVar[dict] = ...
    pattern: Incomplete
    raw_pattern: Incomplete
    include: Incomplete
    relative_to: Incomplete
    def __init__(self, _cls, pattern: Pattern, raw_pattern: str, include: bool | None = ..., relative_to: Path | None = ...) -> None: ...
    def __getnewargs__(self): ...
    @staticmethod
    def compile(pattern: str, _, definition_file: Path) -> _IgnoreRule | None: ...
    @staticmethod
    def match(path: Path, rules: list[_IgnoreRule]) -> bool: ...
def TemporaryDirectory(*args, **kwargs): ...
def mkdirs(path, mode): ...
def correct_maybe_zipped(fileloc: None | str | Path) -> None | str | Path: ...
def open_maybe_zipped(fileloc, mode: str = ...): ...
def find_path_from_directory(base_dir_path: str | os.PathLike[str], ignore_file_name: str, ignore_file_syntax: str = ...) -> Generator[str, None, None]: ...
def list_py_file_paths(directory: str | os.PathLike[str] | None, safe_mode: bool = ..., include_examples: bool | None = ...) -> list[str]: ...
def find_dag_file_paths(directory: str | os.PathLike[str], safe_mode: bool) -> list[str]: ...
def might_contain_dag(file_path: str, safe_mode: bool, zip_file: zipfile.ZipFile | None = ...) -> bool: ...
def might_contain_dag_via_default_heuristic(file_path: str, zip_file: zipfile.ZipFile | None = ...) -> bool: ...
def iter_airflow_imports(file_path: str) -> Generator[str, None, None]: ...
def get_unique_dag_module_name(file_path: str) -> str: ...
