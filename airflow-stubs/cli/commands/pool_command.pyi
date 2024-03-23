import airflow.utils.cli as cli_utils
from airflow.api.client import get_current_api_client as get_current_api_client
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.exceptions import PoolNotFound as PoolNotFound
from airflow.utils.cli import suppress_logs_and_warning as suppress_logs_and_warning
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded

def pool_list(*args, **kwargs): ...
def pool_get(*args, **kwargs): ...
def pool_set(*args, **kwargs): ...
def pool_delete(*args, **kwargs): ...
def pool_import(*args, **kwargs): ...
def pool_export(*args, **kwargs): ...
def pool_import_helper(filepath): ...
def pool_export_helper(filepath): ...
