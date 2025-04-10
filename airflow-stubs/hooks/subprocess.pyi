from _typeshed import Incomplete
from airflow.hooks.base import BaseHook as BaseHook
from subprocess import Popen
from typing import Iterator, NamedTuple

class SubprocessResult(NamedTuple):
    exit_code: Incomplete
    output: Incomplete

def working_directory(cwd: str | None = None) -> Iterator[str]: ...

class SubprocessHook(BaseHook):
    sub_process: Popen[bytes] | None
    def __init__(self, **kwargs) -> None: ...
    def run_command(self, command: list[str], env: dict[str, str] | None = None, output_encoding: str = 'utf-8', cwd: str | None = None) -> SubprocessResult: ...
    def send_sigterm(self) -> None: ...
