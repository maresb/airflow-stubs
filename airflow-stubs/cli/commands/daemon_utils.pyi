from airflow import settings as settings
from airflow.utils.cli import setup_locations as setup_locations, setup_logging as setup_logging, sigint_handler as sigint_handler, sigquit_handler as sigquit_handler
from airflow.utils.process_utils import check_if_pidfile_process_is_running as check_if_pidfile_process_is_running
from argparse import Namespace
from typing import Callable

def run_command_with_daemon_option(*, args: Namespace, process_name: str, callback: Callable, should_setup_logging: bool = False, umask: str = ..., pid_file: str | None = None): ...
