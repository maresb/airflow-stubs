import airflow.settings as settings
from airflow.utils.cli import setup_locations as setup_locations, setup_logging as setup_logging, sigint_handler as sigint_handler, sigquit_handler as sigquit_handler
from airflow.utils.process_utils import check_if_pidfile_process_is_running as check_if_pidfile_process_is_running

def run_command_with_daemon_option(): ...
