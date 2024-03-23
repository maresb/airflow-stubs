import airflow.utils.cli as cli_utils
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.cli.utils import print_export_output as print_export_output
from airflow.models.variable import Variable as Variable
from airflow.utils.cli import suppress_logs_and_warning as suppress_logs_and_warning
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.utils.session import create_session as create_session, provide_session as provide_session

def variables_list(*args, **kwargs): ...
def variables_get(*args, **kwargs): ...
def variables_set(*args, **kwargs): ...
def variables_delete(*args, **kwargs): ...
def variables_import(*args, **kwargs): ...
def variables_export(*args, **kwargs): ...