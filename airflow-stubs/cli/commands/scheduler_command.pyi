import airflow.settings as settings
import airflow.utils.cli as cli_utils
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.cli.commands.daemon_utils import run_command_with_daemon_option as run_command_with_daemon_option
from airflow.configuration import conf as conf
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.job import Job as Job, run_job as run_job
from airflow.jobs.scheduler_job_runner import SchedulerJobRunner as SchedulerJobRunner
from airflow.utils.cli import process_subdir as process_subdir
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.utils.scheduler_health import serve_health_check as serve_health_check
from argparse import Namespace

def scheduler(*args: Namespace, **kwargs): ...
