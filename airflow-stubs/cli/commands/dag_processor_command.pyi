from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.cli.commands.daemon_utils import run_command_with_daemon_option as run_command_with_daemon_option
from airflow.configuration import conf as conf
from airflow.dag_processing.manager import DagFileProcessorManager as DagFileProcessorManager, reload_configuration_for_dag_processing as reload_configuration_for_dag_processing
from airflow.jobs.dag_processor_job_runner import DagProcessorJobRunner as DagProcessorJobRunner
from airflow.jobs.job import Job as Job, run_job as run_job
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded

log: Incomplete

def dag_processor(args): ...
