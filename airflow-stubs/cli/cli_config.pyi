import argparse
from _typeshed import Incomplete
from airflow import settings as settings
from airflow.cli.commands.legacy_commands import check_legacy_command as check_legacy_command
from airflow.configuration import conf as conf
from airflow.utils.cli import ColorMode as ColorMode
from airflow.utils.module_loading import import_string as import_string
from airflow.utils.state import DagRunState as DagRunState, JobState as JobState
from typing import Callable, Iterable, NamedTuple

BUILD_DOCS: Incomplete

def lazy_load_command(import_path: str) -> Callable: ...

class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message) -> None: ...

class Arg:
    flags: Incomplete
    kwargs: Incomplete
    def __init__(self, flags=..., help=..., action=..., default=..., nargs=..., type=..., choices=..., required=..., metavar=..., dest=...) -> None: ...
    def add_to_parser(self, parser: argparse.ArgumentParser): ...

def positive_int(*, allow_zero): ...
def string_list_type(val): ...
def string_lower_type(val): ...

ARG_DAG_ID: Incomplete
ARG_TASK_ID: Incomplete
ARG_EXECUTION_DATE: Incomplete
ARG_EXECUTION_DATE_OPTIONAL: Incomplete
ARG_EXECUTION_DATE_OR_RUN_ID: Incomplete
ARG_EXECUTION_DATE_OR_RUN_ID_OPTIONAL: Incomplete
ARG_TASK_REGEX: Incomplete
ARG_SUBDIR: Incomplete
ARG_START_DATE: Incomplete
ARG_END_DATE: Incomplete
ARG_OUTPUT_PATH: Incomplete
ARG_DRY_RUN: Incomplete
ARG_PID: Incomplete
ARG_DAEMON: Incomplete
ARG_STDERR: Incomplete
ARG_STDOUT: Incomplete
ARG_LOG_FILE: Incomplete
ARG_YES: Incomplete
ARG_OUTPUT: Incomplete
ARG_COLOR: Incomplete
ARG_VERSION_RANGE: Incomplete
ARG_REVISION_RANGE: Incomplete
ARG_SKIP_SERVE_LOGS: Incomplete
ARG_DAG_ID_REQ_FLAG: Incomplete
ARG_NO_BACKFILL: Incomplete
dagrun_states: Incomplete
ARG_DR_STATE: Incomplete
ARG_DAG_ID_OPT: Incomplete
ARG_LIMIT: Incomplete
job_states: Incomplete
ARG_JOB_STATE: Incomplete
ARG_NUM_EXECUTIONS: Incomplete
ARG_MARK_SUCCESS: Incomplete
ARG_INCLUDE_DESCRIPTIONS: Incomplete
ARG_INCLUDE_EXAMPLES: Incomplete
ARG_INCLUDE_SOURCES: Incomplete
ARG_INCLUDE_ENV_VARS: Incomplete
ARG_COMMENT_OUT_EVERYTHING: Incomplete
ARG_EXCLUDE_PROVIDERS: Incomplete
ARG_DEFAULTS: Incomplete
ARG_VERBOSE: Incomplete
ARG_LOCAL: Incomplete
ARG_DONOT_PICKLE: Incomplete
ARG_BF_IGNORE_DEPENDENCIES: Incomplete
ARG_BF_IGNORE_FIRST_DEPENDS_ON_PAST: Incomplete
ARG_POOL: Incomplete
ARG_DELAY_ON_LIMIT: Incomplete
ARG_RESET_DAG_RUN: Incomplete
ARG_RERUN_FAILED_TASKS: Incomplete
ARG_CONTINUE_ON_FAILURES: Incomplete
ARG_DISABLE_RETRY: Incomplete
ARG_RUN_BACKWARDS: Incomplete
ARG_TREAT_DAG_AS_REGEX: Incomplete
ARG_TREAT_DAG_ID_AS_REGEX: Incomplete
ARG_SHOW_DAGRUN: Incomplete
ARG_IMGCAT_DAGRUN: Incomplete
ARG_SAVE_DAGRUN: Incomplete
ARG_USE_EXECUTOR: Incomplete
ARG_MARK_SUCCESS_PATTERN: Incomplete
ARG_TREE: Incomplete
ARG_SHUT_DOWN_LOGGING: Incomplete
ARG_UPSTREAM: Incomplete
ARG_ONLY_FAILED: Incomplete
ARG_ONLY_RUNNING: Incomplete
ARG_DOWNSTREAM: Incomplete
ARG_EXCLUDE_SUBDAGS: Incomplete
ARG_EXCLUDE_PARENTDAG: Incomplete
ARG_DAG_REGEX: Incomplete
ARG_SAVE: Incomplete
ARG_IMGCAT: Incomplete
ARG_RUN_ID: Incomplete
ARG_CONF: Incomplete
ARG_EXEC_DATE: Incomplete
ARG_REPLACE_MICRO: Incomplete
ARG_DB_TABLES: Incomplete
ARG_DB_CLEANUP_TIMESTAMP: Incomplete
ARG_DB_DRY_RUN: Incomplete
ARG_DB_SKIP_ARCHIVE: Incomplete
ARG_DB_EXPORT_FORMAT: Incomplete
ARG_DB_OUTPUT_PATH: Incomplete
ARG_DB_DROP_ARCHIVES: Incomplete
ARG_DB_RETRY: Incomplete
ARG_DB_RETRY_DELAY: Incomplete
ARG_POOL_NAME: Incomplete
ARG_POOL_SLOTS: Incomplete
ARG_POOL_DESCRIPTION: Incomplete
ARG_POOL_INCLUDE_DEFERRED: Incomplete
ARG_POOL_IMPORT: Incomplete
ARG_POOL_EXPORT: Incomplete
ARG_VAR: Incomplete
ARG_VAR_VALUE: Incomplete
ARG_DEFAULT: Incomplete
ARG_VAR_DESCRIPTION: Incomplete
ARG_DESERIALIZE_JSON: Incomplete
ARG_SERIALIZE_JSON: Incomplete
ARG_VAR_IMPORT: Incomplete
ARG_VAR_EXPORT: Incomplete
ARG_VAR_ACTION_ON_EXISTING_KEY: Incomplete
ARG_PRINCIPAL: Incomplete
ARG_KEYTAB: Incomplete
ARG_KERBEROS_ONE_TIME_MODE: Incomplete
ARG_INTERACTIVE: Incomplete
ARG_FORCE: Incomplete
ARG_RAW: Incomplete
ARG_IGNORE_ALL_DEPENDENCIES: Incomplete
ARG_IGNORE_DEPENDENCIES: Incomplete
ARG_IGNORE_DEPENDS_ON_PAST: Incomplete
ARG_DEPENDS_ON_PAST: Incomplete
ARG_SHIP_DAG: Incomplete
ARG_PICKLE: Incomplete
ARG_JOB_ID: Incomplete
ARG_CFG_PATH: Incomplete
ARG_MAP_INDEX: Incomplete
ARG_READ_FROM_DB: Incomplete
ARG_MIGRATION_TIMEOUT: Incomplete
ARG_DB_RESERIALIZE_DAGS: Incomplete
ARG_DB_VERSION__UPGRADE: Incomplete
ARG_DB_REVISION__UPGRADE: Incomplete
ARG_DB_VERSION__DOWNGRADE: Incomplete
ARG_DB_FROM_VERSION: Incomplete
ARG_DB_REVISION__DOWNGRADE: Incomplete
ARG_DB_FROM_REVISION: Incomplete
ARG_DB_SQL_ONLY: Incomplete
ARG_DB_SKIP_INIT: Incomplete
ARG_DB_USE_MIGRATION_FILES: Incomplete
ARG_PORT: Incomplete
ARG_SSL_CERT: Incomplete
ARG_SSL_KEY: Incomplete
ARG_WORKERS: Incomplete
ARG_WORKERCLASS: Incomplete
ARG_WORKER_TIMEOUT: Incomplete
ARG_HOSTNAME: Incomplete
ARG_DEBUG: Incomplete
ARG_ACCESS_LOGFILE: Incomplete
ARG_ERROR_LOGFILE: Incomplete
ARG_ACCESS_LOGFORMAT: Incomplete
ARG_INTERNAL_API_PORT: Incomplete
ARG_INTERNAL_API_WORKERS: Incomplete
ARG_INTERNAL_API_WORKERCLASS: Incomplete
ARG_INTERNAL_API_WORKER_TIMEOUT: Incomplete
ARG_INTERNAL_API_HOSTNAME: Incomplete
ARG_INTERNAL_API_ACCESS_LOGFILE: Incomplete
ARG_INTERNAL_API_ERROR_LOGFILE: Incomplete
ARG_INTERNAL_API_ACCESS_LOGFORMAT: Incomplete
ARG_NUM_RUNS: Incomplete
ARG_DO_PICKLE: Incomplete
ARG_WITHOUT_MINGLE: Incomplete
ARG_WITHOUT_GOSSIP: Incomplete
ARG_TASK_PARAMS: Incomplete
ARG_POST_MORTEM: Incomplete
ARG_ENV_VARS: Incomplete
ARG_CONN_ID: Incomplete
ARG_CONN_ID_FILTER: Incomplete
ARG_CONN_URI: Incomplete
ARG_CONN_JSON: Incomplete
ARG_CONN_TYPE: Incomplete
ARG_CONN_DESCRIPTION: Incomplete
ARG_CONN_HOST: Incomplete
ARG_CONN_LOGIN: Incomplete
ARG_CONN_PASSWORD: Incomplete
ARG_CONN_SCHEMA: Incomplete
ARG_CONN_PORT: Incomplete
ARG_CONN_EXTRA: Incomplete
ARG_CONN_EXPORT: Incomplete
ARG_CONN_EXPORT_FORMAT: Incomplete
ARG_CONN_EXPORT_FILE_FORMAT: Incomplete
ARG_CONN_SERIALIZATION_FORMAT: Incomplete
ARG_CONN_IMPORT: Incomplete
ARG_CONN_OVERWRITE: Incomplete
ARG_PROVIDER_NAME: Incomplete
ARG_FULL: Incomplete
ARG_ANONYMIZE: Incomplete
ARG_FILE_IO: Incomplete
ARG_SECTION: Incomplete
ARG_OPTION: Incomplete
ARG_OPTIONAL_SECTION: Incomplete
ARG_NAMESPACE: Incomplete
ARG_MIN_PENDING_MINUTES: Incomplete
ARG_JOB_TYPE_FILTER: Incomplete
ARG_JOB_HOSTNAME_FILTER: Incomplete
ARG_JOB_HOSTNAME_CALLABLE_FILTER: Incomplete
ARG_JOB_LIMIT: Incomplete
ARG_ALLOW_MULTIPLE: Incomplete
ARG_CAPACITY: Incomplete
ARG_CLEAR_ONLY: Incomplete
ARG_DAG_LIST_COLUMNS: Incomplete
ALTERNATIVE_CONN_SPECS_ARGS: Incomplete

class ActionCommand(NamedTuple):
    name: str
    help: str
    func: Callable
    args: Iterable[Arg]
    description: str | None = ...
    epilog: str | None = ...
    hide: bool = ...

class GroupCommand(NamedTuple):
    name: str
    help: str
    subcommands: Iterable
    description: str | None = ...
    epilog: str | None = ...
CLICommand = ActionCommand | GroupCommand
DAGS_COMMANDS: Incomplete
TASKS_COMMANDS: Incomplete
POOLS_COMMANDS: Incomplete
VARIABLES_COMMANDS: Incomplete
DB_COMMANDS: Incomplete
CONNECTIONS_COMMANDS: Incomplete
PROVIDERS_COMMANDS: Incomplete
CONFIG_COMMANDS: Incomplete
KUBERNETES_COMMANDS: Incomplete
JOBS_COMMANDS: Incomplete
core_commands: list[CLICommand]
dag_cli_commands: list[CLICommand]
DAG_CLI_DICT: dict[str, CLICommand]
