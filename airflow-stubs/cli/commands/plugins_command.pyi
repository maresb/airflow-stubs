from airflow import plugins_manager as plugins_manager
from airflow.cli.simple_table import AirflowConsole as AirflowConsole
from airflow.plugins_manager import PluginsDirectorySource as PluginsDirectorySource, get_plugin_info as get_plugin_info
from airflow.utils.cli import suppress_logs_and_warning as suppress_logs_and_warning
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded

def dump_plugins(args) -> None: ...
