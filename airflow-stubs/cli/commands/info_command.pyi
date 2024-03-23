import airflow.configuration as configuration
import enum
import typing
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.providers_manager import ProvidersManager as ProvidersManager
from airflow.utils.cli import suppress_logs_and_warning as suppress_logs_and_warning
from airflow.utils.platform import getuser as getuser
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from typing import ClassVar

airflow_version: str

class Anonymizer(typing.Protocol):
    __parameters__: ClassVar[tuple] = ...
    _is_protocol: ClassVar[bool] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def process_path(self, value) -> str: ...
    def process_username(self, value) -> str: ...
    def process_url(self, value) -> str: ...
    def __subclasshook__(self, other): ...
    def __init__(self, *args, **kwargs) -> None: ...

class NullAnonymizer(Anonymizer):
    __parameters__: ClassVar[tuple] = ...
    _is_protocol: ClassVar[bool] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def process_path(self, value) -> str: ...
    def process_username(self, value) -> str: ...
    def process_url(self, value) -> str: ...
    def __subclasshook__(self, other): ...

class PiiAnonymizer(Anonymizer):
    __parameters__: ClassVar[tuple] = ...
    _is_protocol: ClassVar[bool] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    def __init__(self) -> None: ...
    def process_path(self, value) -> str: ...
    def process_username(self, value) -> str: ...
    def process_url(self, value) -> str: ...
    def __subclasshook__(self, other): ...

class OperatingSystem(enum.Enum):
    _member_names_: ClassVar[list] = ...
    _member_map_: ClassVar[dict] = ...
    _member_type_: ClassVar[type[object]] = ...
    _value2member_map_: ClassVar[dict] = ...
    WINDOWS: ClassVar[OperatingSystem] = ...
    LINUX: ClassVar[OperatingSystem] = ...
    MACOSX: ClassVar[OperatingSystem] = ...
    CYGWIN: ClassVar[OperatingSystem] = ...
    UNKNOWN: ClassVar[OperatingSystem] = ...
    @staticmethod
    def get_current() -> OperatingSystem: ...
    @classmethod
    def __init__(cls, value) -> None: ...

class Architecture(enum.Enum):
    _member_names_: ClassVar[list] = ...
    _member_map_: ClassVar[dict] = ...
    _member_type_: ClassVar[type[object]] = ...
    _value2member_map_: ClassVar[dict] = ...
    X86_64: ClassVar[Architecture] = ...
    X86: ClassVar[Architecture] = ...
    PPC: ClassVar[Architecture] = ...
    ARM: ClassVar[Architecture] = ...
    UNKNOWN: ClassVar[Architecture] = ...
    @staticmethod
    def get_current() -> Architecture: ...
    @classmethod
    def __init__(cls, value) -> None: ...

class AirflowInfo:
    def __init__(self, anonymizer) -> None: ...
    def show(self, output: str, console: AirflowConsole | None = ...) -> None: ...
    def render_text(self, output: str) -> str: ...

class FileIoException(Exception): ...
def show_info(*args, **kwargs): ...
