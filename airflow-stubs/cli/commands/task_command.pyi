import logging
from _typeshed import Incomplete
from airflow import settings as settings
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig, internal_api_call as internal_api_call
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, DagRunNotFound as DagRunNotFound, TaskDeferred as TaskDeferred, TaskInstanceNotFound as TaskInstanceNotFound
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.job import Job as Job, run_job as run_job
from airflow.jobs.local_task_job_runner import LocalTaskJobRunner as LocalTaskJobRunner
from airflow.listeners.listener import get_listener_manager as get_listener_manager
from airflow.models import DagPickle as DagPickle, TaskInstance as TaskInstance
from airflow.models.dag import DAG as DAG
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.operator import Operator as Operator
from airflow.models.param import ParamsDict as ParamsDict
from airflow.models.taskinstance import TaskReturnCode as TaskReturnCode
from airflow.serialization.pydantic.dag_run import DagRunPydantic as DagRunPydantic
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.settings import IS_EXECUTOR_CONTAINER as IS_EXECUTOR_CONTAINER, IS_K8S_EXECUTOR_POD as IS_K8S_EXECUTOR_POD
from airflow.ti_deps.dep_context import DepContext as DepContext
from airflow.ti_deps.dependencies_deps import SCHEDULER_QUEUED_DEPS as SCHEDULER_QUEUED_DEPS
from airflow.typing_compat import Literal as Literal
from airflow.utils.cli import get_dag as get_dag, get_dag_by_file_location as get_dag_by_file_location, get_dag_by_pickle as get_dag_by_pickle, get_dags as get_dags, should_ignore_depends_on_past as should_ignore_depends_on_past, suppress_logs_and_warning as suppress_logs_and_warning
from airflow.utils.dates import timezone as timezone
from airflow.utils.log.logging_mixin import StreamLogWriter as StreamLogWriter
from airflow.utils.log.secrets_masker import RedactedIO as RedactedIO
from airflow.utils.net import get_hostname as get_hostname
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.utils.session import NEW_SESSION as NEW_SESSION, create_session as create_session, provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState
from airflow.utils.task_instance_session import set_current_task_instance_session as set_current_task_instance_session
from sqlalchemy.orm.session import Session as Session
from typing import Protocol

log: Incomplete
CreateIfNecessary: Incomplete
RAW_TASK_UNSUPPORTED_OPTION: Incomplete

class TaskCommandMarker: ...

def task_run(args, dag: DAG | None = None) -> TaskReturnCode | None: ...
def task_failed_deps(args) -> None: ...
def task_state(args) -> None: ...
def task_list(args, dag: DAG | None = None) -> None: ...

class _SupportedDebugger(Protocol):
    def post_mortem(self) -> None: ...

SUPPORTED_DEBUGGER_MODULES: Incomplete

def task_states_for_dag_run(args, session: Session = ...) -> None: ...
def task_test(args, dag: DAG | None = None, session: Session = ...) -> None: ...
def task_render(args, dag: DAG | None = None) -> None: ...
def task_clear(args) -> None: ...

class LoggerMutationHelper:
    handlers: Incomplete
    level: Incomplete
    propagate: Incomplete
    source_logger: Incomplete
    def __init__(self, logger: logging.Logger) -> None: ...
    def apply(self, logger: logging.Logger, replace: bool = True) -> None: ...
    def move(self, logger: logging.Logger, replace: bool = True) -> None: ...
    def reset(self) -> None: ...
    def __enter__(self) -> LoggerMutationHelper: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
