import airflow.settings as settings
import argparse
from _typeshed import Incomplete
from airflow.cli.commands.legacy_commands import check_legacy_command as check_legacy_command
from airflow.configuration import conf as conf
from airflow.utils.cli import ColorMode as ColorMode
from airflow.utils.module_loading import import_string as import_string
from airflow.utils.state import DagRunState as DagRunState, JobState as JobState
from airflow.utils.timezone import parsedate as parsedate
from typing import Callable, ClassVar, Iterable

BUILD_DOCS: bool
def lazy_load_command(import_path: str) -> Callable: ...

class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message): ...

class Arg:
    def __init__(self, flags: object = ..., help: object = ..., action: object = ..., default: object = ..., nargs: object = ..., type: object = ..., choices: object = ..., required: object = ..., metavar: object = ..., dest: object = ...) -> None: ...
    def add_to_parser(self, parser: argparse.ArgumentParser): ...
def positive_int(): ...
def string_list_type(val): ...
def string_lower_type(val): ...

ARG_DAG_ID: Arg
ARG_TASK_ID: Arg
ARG_EXECUTION_DATE: Arg
ARG_EXECUTION_DATE_OPTIONAL: Arg
ARG_EXECUTION_DATE_OR_RUN_ID: Arg
ARG_EXECUTION_DATE_OR_RUN_ID_OPTIONAL: Arg
ARG_TASK_REGEX: Arg
ARG_SUBDIR: Arg
ARG_START_DATE: Arg
ARG_END_DATE: Arg
ARG_OUTPUT_PATH: Arg
ARG_DRY_RUN: Arg
ARG_PID: Arg
ARG_DAEMON: Arg
ARG_STDERR: Arg
ARG_STDOUT: Arg
ARG_LOG_FILE: Arg
ARG_YES: Arg
ARG_OUTPUT: Arg
ARG_COLOR: Arg
ARG_VERSION_RANGE: Arg
ARG_REVISION_RANGE: Arg
ARG_SKIP_SERVE_LOGS: Arg
ARG_DAG_ID_REQ_FLAG: Arg
ARG_NO_BACKFILL: Arg
dagrun_states: tuple
ARG_DR_STATE: Arg
ARG_DAG_ID_OPT: Arg
ARG_LIMIT: Arg
job_states: tuple
ARG_JOB_STATE: Arg
ARG_NUM_EXECUTIONS: Arg
ARG_MARK_SUCCESS: Arg
ARG_INCLUDE_DESCRIPTIONS: Arg
ARG_INCLUDE_EXAMPLES: Arg
ARG_INCLUDE_SOURCES: Arg
ARG_INCLUDE_ENV_VARS: Arg
ARG_COMMENT_OUT_EVERYTHING: Arg
ARG_EXCLUDE_PROVIDERS: Arg
ARG_DEFAULTS: Arg
ARG_VERBOSE: Arg
ARG_LOCAL: Arg
ARG_DONOT_PICKLE: Arg
ARG_BF_IGNORE_DEPENDENCIES: Arg
ARG_BF_IGNORE_FIRST_DEPENDS_ON_PAST: Arg
ARG_POOL: Arg
ARG_DELAY_ON_LIMIT: Arg
ARG_RESET_DAG_RUN: Arg
ARG_RERUN_FAILED_TASKS: Arg
ARG_CONTINUE_ON_FAILURES: Arg
ARG_DISABLE_RETRY: Arg
ARG_RUN_BACKWARDS: Arg
ARG_TREAT_DAG_AS_REGEX: Arg
ARG_SHOW_DAGRUN: Arg
ARG_IMGCAT_DAGRUN: Arg
ARG_SAVE_DAGRUN: Arg
ARG_TREE: Arg
ARG_SHUT_DOWN_LOGGING: Arg
ARG_UPSTREAM: Arg
ARG_ONLY_FAILED: Arg
ARG_ONLY_RUNNING: Arg
ARG_DOWNSTREAM: Arg
ARG_EXCLUDE_SUBDAGS: Arg
ARG_EXCLUDE_PARENTDAG: Arg
ARG_DAG_REGEX: Arg
ARG_SAVE: Arg
ARG_IMGCAT: Arg
ARG_RUN_ID: Arg
ARG_CONF: Arg
ARG_EXEC_DATE: Arg
ARG_REPLACE_MICRO: Arg
ARG_DB_TABLES: Arg
ARG_DB_CLEANUP_TIMESTAMP: Arg
ARG_DB_DRY_RUN: Arg
ARG_DB_SKIP_ARCHIVE: Arg
ARG_DB_EXPORT_FORMAT: Arg
ARG_DB_OUTPUT_PATH: Arg
ARG_DB_DROP_ARCHIVES: Arg
ARG_DB_RETRY: Arg
ARG_DB_RETRY_DELAY: Arg
ARG_POOL_NAME: Arg
ARG_POOL_SLOTS: Arg
ARG_POOL_DESCRIPTION: Arg
ARG_POOL_INCLUDE_DEFERRED: Arg
ARG_POOL_IMPORT: Arg
ARG_POOL_EXPORT: Arg
ARG_VAR: Arg
ARG_VAR_VALUE: Arg
ARG_DEFAULT: Arg
ARG_VAR_DESCRIPTION: Arg
ARG_DESERIALIZE_JSON: Arg
ARG_SERIALIZE_JSON: Arg
ARG_VAR_IMPORT: Arg
ARG_VAR_EXPORT: Arg
ARG_VAR_ACTION_ON_EXISTING_KEY: Arg
ARG_PRINCIPAL: Arg
ARG_KEYTAB: Arg
ARG_KERBEROS_ONE_TIME_MODE: Arg
ARG_INTERACTIVE: Arg
ARG_FORCE: Arg
ARG_RAW: Arg
ARG_IGNORE_ALL_DEPENDENCIES: Arg
ARG_IGNORE_DEPENDENCIES: Arg
ARG_IGNORE_DEPENDS_ON_PAST: Arg
ARG_DEPENDS_ON_PAST: Arg
ARG_SHIP_DAG: Arg
ARG_PICKLE: Arg
ARG_JOB_ID: Arg
ARG_CFG_PATH: Arg
ARG_MAP_INDEX: Arg
ARG_READ_FROM_DB: Arg
ARG_MIGRATION_TIMEOUT: Arg
ARG_DB_RESERIALIZE_DAGS: Arg
ARG_DB_VERSION__UPGRADE: Arg
ARG_DB_REVISION__UPGRADE: Arg
ARG_DB_VERSION__DOWNGRADE: Arg
ARG_DB_FROM_VERSION: Arg
ARG_DB_REVISION__DOWNGRADE: Arg
ARG_DB_FROM_REVISION: Arg
ARG_DB_SQL_ONLY: Arg
ARG_DB_SKIP_INIT: Arg
ARG_PORT: Arg
ARG_SSL_CERT: Arg
ARG_SSL_KEY: Arg
ARG_WORKERS: Arg
ARG_WORKERCLASS: Arg
ARG_WORKER_TIMEOUT: Arg
ARG_HOSTNAME: Arg
ARG_DEBUG: Arg
ARG_ACCESS_LOGFILE: Arg
ARG_ERROR_LOGFILE: Arg
ARG_ACCESS_LOGFORMAT: Arg
ARG_INTERNAL_API_PORT: Arg
ARG_INTERNAL_API_WORKERS: Arg
ARG_INTERNAL_API_WORKERCLASS: Arg
ARG_INTERNAL_API_WORKER_TIMEOUT: Arg
ARG_INTERNAL_API_HOSTNAME: Arg
ARG_INTERNAL_API_ACCESS_LOGFILE: Arg
ARG_INTERNAL_API_ERROR_LOGFILE: Arg
ARG_INTERNAL_API_ACCESS_LOGFORMAT: Arg
ARG_NUM_RUNS: Arg
ARG_DO_PICKLE: Arg
ARG_WITHOUT_MINGLE: Arg
ARG_WITHOUT_GOSSIP: Arg
ARG_TASK_PARAMS: Arg
ARG_POST_MORTEM: Arg
ARG_ENV_VARS: Arg
ARG_CONN_ID: Arg
ARG_CONN_ID_FILTER: Arg
ARG_CONN_URI: Arg
ARG_CONN_JSON: Arg
ARG_CONN_TYPE: Arg
ARG_CONN_DESCRIPTION: Arg
ARG_CONN_HOST: Arg
ARG_CONN_LOGIN: Arg
ARG_CONN_PASSWORD: Arg
ARG_CONN_SCHEMA: Arg
ARG_CONN_PORT: Arg
ARG_CONN_EXTRA: Arg
ARG_CONN_EXPORT: Arg
ARG_CONN_EXPORT_FORMAT: Arg
ARG_CONN_EXPORT_FILE_FORMAT: Arg
ARG_CONN_SERIALIZATION_FORMAT: Arg
ARG_CONN_IMPORT: Arg
ARG_CONN_OVERWRITE: Arg
ARG_PROVIDER_NAME: Arg
ARG_FULL: Arg
ARG_ANONYMIZE: Arg
ARG_FILE_IO: Arg
ARG_SECTION: Arg
ARG_OPTION: Arg
ARG_OPTIONAL_SECTION: Arg
ARG_NAMESPACE: Arg
ARG_MIN_PENDING_MINUTES: Arg
ARG_JOB_TYPE_FILTER: Arg
ARG_JOB_HOSTNAME_FILTER: Arg
ARG_JOB_HOSTNAME_CALLABLE_FILTER: Arg
ARG_JOB_LIMIT: Arg
ARG_ALLOW_MULTIPLE: Arg
ARG_CAPACITY: Arg
ARG_CLEAR_ONLY: Arg
ALTERNATIVE_CONN_SPECS_ARGS: list

class ActionCommand(tuple):
    _fields: ClassVar[tuple] = ...
    _field_defaults: ClassVar[dict] = ...
    _fields_defaults: ClassVar[dict] = ...
    _field_types: ClassVar[dict] = ...
    name: Incomplete
    help: Incomplete
    func: Incomplete
    args: Incomplete
    description: Incomplete
    epilog: Incomplete
    hide: Incomplete
    def __init__(self, _cls, name: str, help: str, func: Callable, args: Iterable[Arg], description: str | None = ..., epilog: str | None = ..., hide: bool = ...) -> None: ...
    def __getnewargs__(self): ...

class GroupCommand(tuple):
    _fields: ClassVar[tuple] = ...
    _field_defaults: ClassVar[dict] = ...
    _fields_defaults: ClassVar[dict] = ...
    _field_types: ClassVar[dict] = ...
    name: Incomplete
    help: Incomplete
    subcommands: Incomplete
    description: Incomplete
    epilog: Incomplete
    def __init__(self, _cls, name: str, help: str, subcommands: Iterable, description: str | None = ..., epilog: str | None = ...) -> None: ...
    def __getnewargs__(self): ...
DAGS_COMMANDS: tuple
TASKS_COMMANDS: tuple
POOLS_COMMANDS: tuple
VARIABLES_COMMANDS: tuple
DB_COMMANDS: tuple
CONNECTIONS_COMMANDS: tuple
PROVIDERS_COMMANDS: tuple
CONFIG_COMMANDS: tuple
KUBERNETES_COMMANDS: tuple
JOBS_COMMANDS: tuple
core_commands: list
dag_cli_commands: list
DAG_CLI_DICT: dict
