import airflow.settings as settings
import airflow.utils.cli as cli_utils
from airflow.cli.commands.daemon_utils import run_command_with_daemon_option as run_command_with_daemon_option
from airflow.configuration import conf as conf
from airflow.jobs.job import Job as Job, run_job as run_job
from airflow.jobs.triggerer_job_runner import TriggererJobRunner as TriggererJobRunner
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.utils.serve_logs import serve_logs as serve_logs

def triggerer_run(skip_serve_logs: bool, capacity: int, triggerer_heartrate: float): ...
def triggerer(*args, **kwargs): ...
