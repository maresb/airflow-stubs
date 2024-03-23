import airflow.utils.log.logging_mixin
import subprocess
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.utils.configuration import tmp_configuration_copy as tmp_configuration_copy
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.platform import getuser as getuser

IS_WINDOWS: bool
TYPE_CHECKING: bool
PYTHONPATH_VAR: str

class BaseTaskRunner(airflow.utils.log.logging_mixin.LoggingMixin):
    def __init__(self, job_runner: LocalTaskJobRunner) -> None: ...
    def run_command(self, run_with: Incomplete | None = ...) -> subprocess.Popen: ...
    def start(self): ...
    def return_code(self, timeout: float = ...) -> int | None: ...
    def terminate(self) -> None: ...
    def on_finish(self) -> None: ...
    def get_process_pid(self) -> int: ...
