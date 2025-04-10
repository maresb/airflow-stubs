from _typeshed import Incomplete
from airflow import settings as settings
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.cli.commands.daemon_utils import run_command_with_daemon_option as run_command_with_daemon_option
from airflow.cli.commands.webserver_command import GunicornMonitor as GunicornMonitor
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.logging_config import configure_logging as configure_logging
from airflow.models import import_all_models as import_all_models
from airflow.utils.cli import setup_locations as setup_locations
from airflow.utils.providers_configuration_loader import providers_configuration_loaded as providers_configuration_loaded
from airflow.www.extensions.init_dagbag import init_dagbag as init_dagbag
from airflow.www.extensions.init_jinja_globals import init_jinja_globals as init_jinja_globals
from airflow.www.extensions.init_manifest_files import configure_manifest_files as configure_manifest_files
from airflow.www.extensions.init_security import init_xframe_protection as init_xframe_protection
from airflow.www.extensions.init_views import init_api_internal as init_api_internal, init_error_handlers as init_error_handlers
from flask import Flask

log: Incomplete
app: Flask | None

def internal_api(args): ...
def create_app(config: Incomplete | None = None, testing: bool = False): ...
def cached_app(config: Incomplete | None = None, testing: bool = False): ...
