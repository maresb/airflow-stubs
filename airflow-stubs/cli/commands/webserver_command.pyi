import airflow.settings as settings
import airflow.utils.cli as cli_utils
import airflow.utils.log.logging_mixin
from airflow.cli.commands.daemon_utils import run_command_with_daemon_option as run_command_with_daemon_option
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, AirflowWebServerTimeout as AirflowWebServerTimeout
from airflow.utils.cli import setup_locations as setup_locations
from airflow.utils.hashlib_wrapper import md5 as md5
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from typing import NoReturn

class GunicornMonitor(airflow.utils.log.logging_mixin.LoggingMixin):
    def __init__(self, gunicorn_master_pid: int, num_workers_expected: int, master_timeout: int, worker_refresh_interval: int, worker_refresh_batch_size: int, reload_on_plugin_change: bool) -> None: ...
    def start(self) -> NoReturn: ...
def webserver(*args, **kwargs): ...
