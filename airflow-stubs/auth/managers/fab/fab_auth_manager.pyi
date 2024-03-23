import airflow.auth.managers.base_auth_manager
import airflow.security.permissions as permissions
import functools
from airflow.auth.managers.base_auth_manager import BaseAuthManager as BaseAuthManager
from airflow.auth.managers.fab.models import Permission as Permission, Role as Role, User as User
from airflow.auth.managers.models.resource_details import AccessView as AccessView, ConfigurationDetails as ConfigurationDetails, ConnectionDetails as ConnectionDetails, DagAccessEntity as DagAccessEntity, DagDetails as DagDetails, DatasetDetails as DatasetDetails, PoolDetails as PoolDetails, VariableDetails as VariableDetails
from airflow.auth.managers.utils.fab import get_fab_action_from_method_map as get_fab_action_from_method_map, get_method_from_fab_action_map as get_method_from_fab_action_map
from airflow.cli.cli_config import GroupCommand as GroupCommand, SYNC_PERM_COMMAND as SYNC_PERM_COMMAND
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowException as AirflowException
from airflow.models.dag import DagModel as DagModel
from airflow.utils.session import provide_session as provide_session
from airflow.utils.yaml import safe_load as safe_load
from connexion.apis.flask_api import FlaskApi
from typing import ClassVar

TYPE_CHECKING: bool
ROLES_COMMANDS: tuple
USERS_COMMANDS: tuple
RESOURCE_AUDIT_LOG: str
RESOURCE_CLUSTER_ACTIVITY: str
RESOURCE_CONFIG: str
RESOURCE_CONNECTION: str
RESOURCE_DAG: str
RESOURCE_DAG_CODE: str
RESOURCE_DAG_DEPENDENCIES: str
RESOURCE_DAG_PREFIX: str
RESOURCE_DAG_RUN: str
RESOURCE_DAG_WARNING: str
RESOURCE_DATASET: str
RESOURCE_DOCS: str
RESOURCE_IMPORT_ERROR: str
RESOURCE_JOB: str
RESOURCE_PLUGIN: str
RESOURCE_POOL: str
RESOURCE_PROVIDER: str
RESOURCE_SLA_MISS: str
RESOURCE_TASK_INSTANCE: str
RESOURCE_TASK_LOG: str
RESOURCE_TASK_RESCHEDULE: str
RESOURCE_TRIGGER: str
RESOURCE_VARIABLE: str
RESOURCE_WEBSITE: str
RESOURCE_XCOM: str
NEW_SESSION: None

class FabAuthManager(airflow.auth.managers.base_auth_manager.BaseAuthManager):
    security_manager: ClassVar[functools.cached_property] = ...
    @staticmethod
    def get_cli_commands() -> list[CLICommand]: ...
    def get_api_endpoints(self) -> None | FlaskApi: ...
    def get_user_display_name(self) -> str: ...
    def get_user(self) -> User: ...
    def init(self) -> None: ...
    def is_logged_in(self) -> bool: ...
    def is_authorized_configuration(self) -> bool: ...
    def is_authorized_cluster_activity(self) -> bool: ...
    def is_authorized_connection(self) -> bool: ...
    def is_authorized_dag(self) -> bool: ...
    def is_authorized_dataset(self) -> bool: ...
    def is_authorized_pool(self) -> bool: ...
    def is_authorized_variable(self) -> bool: ...
    def is_authorized_view(self) -> bool: ...
    def is_authorized_custom_view(self): ...
    def get_permitted_dag_ids(self, *args, **kwargs) -> set[str]: ...
    def get_url_login(self, **kwargs) -> str: ...
    def get_url_logout(self): ...
    def get_url_user_profile(self) -> str | None: ...
