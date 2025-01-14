import airflow.executors.executor_constants as executor_constants
import airflow.utils.db as db
import threading
from airflow.configuration import conf as conf
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.job import most_recent_job as most_recent_job
from airflow.jobs.scheduler_job_runner import SchedulerJobRunner as SchedulerJobRunner
from airflow.jobs.triggerer_job_runner import TriggererJobRunner as TriggererJobRunner
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded

TYPE_CHECKING: bool

class StandaloneCommand:
    @classmethod
    def entrypoint(cls, args): ...
    def __init__(self) -> None: ...
    def run(self, *args, **kwargs): ...
    def update_output(self): ...
    def print_output(self, name: str, output): ...
    def print_error(self, name: str, output): ...
    def calculate_env(self): ...
    def initialize_database(self): ...
    def is_ready(self): ...
    def port_open(self, port): ...
    def job_running(self, job_runner_class: type[BaseJobRunner]): ...
    def print_ready(self): ...

class SubCommand(threading.Thread):
    def __init__(self, parent, name: str, command: list[str], env: dict[str, str]) -> None: ...
    def run(self): ...
    def stop(self): ...
standalone: method
