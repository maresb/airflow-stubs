from _typeshed import Incomplete
from airflow.plugins_manager import PluginsDirectorySource as PluginsDirectorySource
from airflow.typing_compat import TypeGuard as TypeGuard
from airflow.utils import yaml as yaml
from airflow.utils.platform import is_tty as is_tty
from rich.console import Console
from rich.table import Table
from typing import Any, Callable, Sequence

def is_data_sequence(data: Sequence[dict | Any]) -> TypeGuard[Sequence[dict]]: ...

class AirflowConsole(Console):
    show_header: Incomplete
    def __init__(self, show_header: bool = True, *args, **kwargs) -> None: ...
    def print_as_json(self, data: dict): ...
    def print_as_yaml(self, data: dict): ...
    def print_as_table(self, data: list[dict]): ...
    def print_as_plain_table(self, data: list[dict]): ...
    def print_as(self, data: Sequence[dict | Any], output: str, mapper: Callable[[Any], dict] | None = None) -> None: ...

class SimpleTable(Table):
    show_edge: Incomplete
    pad_edge: Incomplete
    box: Incomplete
    show_header: Incomplete
    title_style: Incomplete
    title_justify: Incomplete
    caption: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def add_column(self, *args, **kwargs) -> None: ...
