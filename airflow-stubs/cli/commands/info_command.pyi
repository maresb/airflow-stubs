from _typeshed import Incomplete
from airflow import configuration as configuration
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.providers_manager import ProvidersManager as ProvidersManager
from airflow.typing_compat import Protocol as Protocol
from airflow.utils.cli import suppress_logs_and_warning as suppress_logs_and_warning
from airflow.utils.platform import getuser as getuser
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from enum import Enum

log: Incomplete

class Anonymizer(Protocol):
    def process_path(self, value) -> str: ...
    def process_username(self, value) -> str: ...
    def process_url(self, value) -> str: ...

class NullAnonymizer(Anonymizer):
    process_path: Incomplete
    process_username: Incomplete
    process_url: Incomplete

class PiiAnonymizer(Anonymizer):
    def __init__(self) -> None: ...
    def process_path(self, value) -> str: ...
    def process_username(self, value) -> str: ...
    def process_url(self, value) -> str: ...

class OperatingSystem(Enum):
    WINDOWS = 'Windows'
    LINUX = 'Linux'
    MACOSX = 'Mac OS'
    CYGWIN = 'Cygwin'
    UNKNOWN = 'Unknown'
    @staticmethod
    def get_current() -> OperatingSystem: ...

class Architecture(Enum):
    X86_64 = 'x86_64'
    X86 = 'x86'
    PPC = 'ppc'
    ARM = 'arm'
    UNKNOWN = 'unknown'
    @staticmethod
    def get_current() -> Architecture: ...

class AirflowInfo:
    anonymizer: Incomplete
    def __init__(self, anonymizer) -> None: ...
    def show(self, output: str, console: AirflowConsole | None = None) -> None: ...
    def render_text(self, output: str) -> str: ...

class FileIoException(Exception): ...

def show_info(args) -> None: ...
