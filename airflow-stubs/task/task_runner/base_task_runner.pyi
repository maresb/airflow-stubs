import subprocess
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.jobs.local_task_job_runner import LocalTaskJobRunner as LocalTaskJobRunner
from airflow.utils.configuration import tmp_configuration_copy as tmp_configuration_copy
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.platform import IS_WINDOWS as IS_WINDOWS, getuser as getuser
from pwd import getpwnam as getpwnam

PYTHONPATH_VAR: str

class BaseTaskRunner(LoggingMixin):
    job_runner: Incomplete
    run_as_user: str | None
    process: Incomplete
    def __init__(self, job_runner: LocalTaskJobRunner) -> None: ...
    def run_command(self, run_with: Incomplete | None = None) -> subprocess.Popen: ...
    def start(self) -> None: ...
    def return_code(self, timeout: float = 0.0) -> int | None: ...
    def terminate(self) -> None: ...
    def on_finish(self) -> None: ...
    def get_process_pid(self) -> int: ...
