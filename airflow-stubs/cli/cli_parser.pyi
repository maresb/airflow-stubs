import functools
import rich_argparse
from airflow.auth.managers.fab.fab_auth_manager import auth_mgr as auth_mgr
from airflow.cli.cli_config import ActionCommand as ActionCommand, DefaultHelpParser as DefaultHelpParser, GroupCommand as GroupCommand
from airflow.cli.utils import CliConflictError as CliConflictError
from airflow.exceptions import AirflowException as AirflowException
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader, _ as _
from airflow.executors.sequential_executor import executor as executor
from airflow.utils.helpers import partition as partition
from airflow.www.extensions.init_auth_manager import get_auth_manager_cls as get_auth_manager_cls
from argparse import Action

TYPE_CHECKING: bool
DAG_CLI_DICT: dict
core_commands: list
airflow_commands: list
ALL_COMMANDS_DICT: dict

class AirflowHelpFormatter(rich_argparse.RichHelpFormatter): ...

class LazyRichHelpFormatter(rich_argparse.RawTextRichHelpFormatter):
    def add_argument(self, action: Action) -> None: ...
get_parser: functools._lru_cache_wrapper
