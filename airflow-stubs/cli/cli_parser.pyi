import argparse
from _typeshed import Incomplete
from airflow.cli.cli_config import ActionCommand as ActionCommand, Arg as Arg, CLICommand as CLICommand, DAG_CLI_DICT as DAG_CLI_DICT, DefaultHelpParser as DefaultHelpParser, GroupCommand as GroupCommand, core_commands as core_commands
from airflow.cli.utils import CliConflictError as CliConflictError
from airflow.exceptions import AirflowException as AirflowException
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.utils.helpers import partition as partition
from airflow.www.extensions.init_auth_manager import get_auth_manager_cls as get_auth_manager_cls
from argparse import Action
from rich_argparse import RawTextRichHelpFormatter, RichHelpFormatter

airflow_commands: Incomplete
log: Incomplete
executor: Incomplete
_: Incomplete
auth_mgr: Incomplete
ALL_COMMANDS_DICT: dict[str, CLICommand]
dup: Incomplete

class AirflowHelpFormatter(RichHelpFormatter): ...

class LazyRichHelpFormatter(RawTextRichHelpFormatter):
    def add_argument(self, action: Action) -> None: ...

def get_parser(dag_parser: bool = False) -> argparse.ArgumentParser: ...
