from _typeshed import Incomplete
from airflow import settings as settings
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException, RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.logging_config import configure_logging as configure_logging
from airflow.models import import_all_models as import_all_models
from airflow.utils.json import AirflowJsonProvider as AirflowJsonProvider
from airflow.www.extensions.init_appbuilder import init_appbuilder as init_appbuilder
from airflow.www.extensions.init_appbuilder_links import init_appbuilder_links as init_appbuilder_links
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from airflow.www.extensions.init_cache import init_cache as init_cache
from airflow.www.extensions.init_dagbag import init_dagbag as init_dagbag
from airflow.www.extensions.init_jinja_globals import init_jinja_globals as init_jinja_globals
from airflow.www.extensions.init_manifest_files import configure_manifest_files as configure_manifest_files
from airflow.www.extensions.init_robots import init_robots as init_robots
from airflow.www.extensions.init_security import init_api_experimental_auth as init_api_experimental_auth, init_cache_control as init_cache_control, init_check_user_active as init_check_user_active, init_xframe_protection as init_xframe_protection
from airflow.www.extensions.init_session import init_airflow_session_interface as init_airflow_session_interface
from airflow.www.extensions.init_views import init_api_auth_provider as init_api_auth_provider, init_api_connexion as init_api_connexion, init_api_error_handlers as init_api_error_handlers, init_api_experimental as init_api_experimental, init_api_internal as init_api_internal, init_appbuilder_views as init_appbuilder_views, init_error_handlers as init_error_handlers, init_flash_views as init_flash_views, init_plugins as init_plugins
from airflow.www.extensions.init_wsgi_middlewares import init_wsgi_middleware as init_wsgi_middleware
from flask import Flask

app: Flask | None
csrf: Incomplete

def create_app(config: Incomplete | None = None, testing: bool = False): ...
def cached_app(config: Incomplete | None = None, testing: bool = False): ...
def purge_cached_app() -> None: ...
