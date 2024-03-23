import airflow.settings as settings
import airflow.utils.cli as cli_utils
import airflow.utils.timezone as timezone
from airflow.api.client import get_current_api_client as get_current_api_client
from airflow.api_connexion.schemas.dag_schema import dag_schema as dag_schema
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.jobs.job import Job as Job
from airflow.models.dag import DAG as DAG, DagModel as DagModel
from airflow.models.dagbag import DagBag as DagBag
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.serialized_dag import SerializedDagModel as SerializedDagModel
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.utils.cli import get_dag as get_dag, get_dags as get_dags, process_subdir as process_subdir, sigint_handler as sigint_handler, suppress_logs_and_warning as suppress_logs_and_warning
from airflow.utils.dot_renderer import render_dag as render_dag, render_dag_dependencies as render_dag_dependencies
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.utils.session import create_session as create_session, provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState

TYPE_CHECKING: bool
NEW_SESSION: None
def dag_backfill(*args, **kwargs) -> None: ...
def dag_trigger(*args, **kwargs) -> None: ...
def dag_delete(*args, **kwargs) -> None: ...
def dag_pause(*args, **kwargs) -> None: ...
def dag_unpause(*args, **kwargs) -> None: ...
def set_is_paused(*args, **kwargs) -> None: ...
def dag_dependencies_show(*args, **kwargs) -> None: ...
def dag_show(*args, **kwargs) -> None: ...
def dag_state(*args, **kwargs) -> None: ...
def dag_next_execution(*args, **kwargs) -> None: ...
def dag_list_dags(*args, **kwargs) -> None: ...
def dag_details(*args, **kwargs): ...
def dag_list_import_errors(*args, **kwargs) -> None: ...
def dag_report(*args, **kwargs) -> None: ...
def dag_list_jobs(*args, **kwargs) -> None: ...
def dag_list_dag_runs(*args, **kwargs) -> None: ...
def dag_test(*args, **kwargs) -> None: ...
def dag_reserialize(*args, **kwargs) -> None: ...
