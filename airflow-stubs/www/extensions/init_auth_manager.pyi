from airflow.auth.managers.base_auth_manager import BaseAuthManager as BaseAuthManager
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.www.extensions.init_appbuilder import AirflowAppBuilder as AirflowAppBuilder

auth_manager: BaseAuthManager | None

def get_auth_manager_cls() -> type[BaseAuthManager]: ...
def init_auth_manager(appbuilder: AirflowAppBuilder) -> BaseAuthManager: ...
def get_auth_manager() -> BaseAuthManager: ...
def is_auth_manager_initialized() -> bool: ...
