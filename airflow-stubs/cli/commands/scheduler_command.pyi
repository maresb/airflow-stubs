from _typeshed import Incomplete
from airflow import settings as settings
from airflow.cli.commands.daemon_utils import run_command_with_daemon_option as run_command_with_daemon_option
from airflow.configuration import conf as conf
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.job import Job as Job, run_job as run_job
from airflow.jobs.scheduler_job_runner import SchedulerJobRunner as SchedulerJobRunner
from airflow.utils.cli import process_subdir as process_subdir
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.utils.scheduler_health import serve_health_check as serve_health_check
from argparse import Namespace

log: Incomplete

def scheduler(args: Namespace): ...
