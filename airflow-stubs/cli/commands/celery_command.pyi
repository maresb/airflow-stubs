import airflow.settings as settings
import airflow.utils.cli as cli_utils
from airflow.cli.commands.daemon_utils import run_command_with_daemon_option as run_command_with_daemon_option
from airflow.configuration import conf as conf
from airflow.utils.cli import setup_locations as setup_locations
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.utils.serve_logs import serve_logs as serve_logs

DEFAULT_TASK_LOG_FMT: str
WORKER_PROCESS_NAME: str
def flower(*args, **kwargs): ...
def logger_setup_handler(*args, **kwargs): ...
def worker(*args, **kwargs): ...
def stop_worker(*args, **kwargs): ...
