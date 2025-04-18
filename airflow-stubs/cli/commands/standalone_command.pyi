import threading
from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.executors import executor_constants as executor_constants
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import most_recent_job as most_recent_job
from airflow.jobs.scheduler_job_runner import SchedulerJobRunner as SchedulerJobRunner
from airflow.jobs.triggerer_job_runner import TriggererJobRunner as TriggererJobRunner
from airflow.utils import db as db
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded

class StandaloneCommand:
    @classmethod
    def entrypoint(cls, args) -> None: ...
    subcommands: Incomplete
    output_queue: Incomplete
    user_info: Incomplete
    ready_time: Incomplete
    ready_delay: int
    def __init__(self) -> None: ...
    web_server_port: Incomplete
    def run(self) -> None: ...
    def update_output(self) -> None: ...
    def print_output(self, name: str, output): ...
    def print_error(self, name: str, output): ...
    def calculate_env(self): ...
    def initialize_database(self) -> None: ...
    def is_ready(self): ...
    def port_open(self, port): ...
    def job_running(self, job_runner_class: type[BaseJobRunner]): ...
    def print_ready(self) -> None: ...

class SubCommand(threading.Thread):
    parent: Incomplete
    name: Incomplete
    command: Incomplete
    env: Incomplete
    def __init__(self, parent, name: str, command: list[str], env: dict[str, str]) -> None: ...
    process: Incomplete
    def run(self) -> None: ...
    def stop(self) -> None: ...

standalone: Incomplete
