import airflow.utils.cli as cli_utils
from airflow.auth.managers.fab.cli_commands.utils import get_application_builder as get_application_builder
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.utils.cli import suppress_logs_and_warning as suppress_logs_and_warning
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded

TYPE_CHECKING: bool
EXISTING_ROLES: set
def roles_list(*args, **kwargs): ...
def roles_create(*args, **kwargs): ...
def roles_delete(*args, **kwargs): ...
def roles_add_perms(*args, **kwargs): ...
def roles_del_perms(*args, **kwargs): ...
def roles_export(*args, **kwargs): ...
def roles_import(*args, **kwargs): ...