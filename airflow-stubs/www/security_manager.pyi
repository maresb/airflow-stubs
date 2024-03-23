import airflow.utils.log.logging_mixin
import functools
from _typeshed import Incomplete
from airflow.auth.managers.models.resource_details import AccessView as AccessView, ConnectionDetails as ConnectionDetails, DagAccessEntity as DagAccessEntity, DagDetails as DagDetails, PoolDetails as PoolDetails, VariableDetails as VariableDetails
from airflow.auth.managers.utils.fab import get_method_from_fab_action_map as get_method_from_fab_action_map
from airflow.exceptions import AirflowException as AirflowException
from airflow.models.connection import Connection as Connection
from airflow.models.dagrun import DagRun as DagRun
from airflow.models.pool import Pool as Pool
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.models.variable import Variable as Variable
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import provide_session as provide_session
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from airflow.www.utils import CustomSQLAInterface as CustomSQLAInterface
from flask_limiter.extension import Limiter
from typing import ClassVar

TYPE_CHECKING: bool
FAB_EXISTING_ROLES: set
RESOURCE_ADMIN_MENU: str
RESOURCE_AUDIT_LOG: str
RESOURCE_BROWSE_MENU: str
RESOURCE_CLUSTER_ACTIVITY: str
RESOURCE_CONFIG: str
RESOURCE_CONNECTION: str
RESOURCE_DAG: str
RESOURCE_DAG_CODE: str
RESOURCE_DAG_DEPENDENCIES: str
RESOURCE_DAG_RUN: str
RESOURCE_DATASET: str
RESOURCE_DOCS: str
RESOURCE_DOCS_MENU: str
RESOURCE_JOB: str
RESOURCE_PLUGIN: str
RESOURCE_POOL: str
RESOURCE_PROVIDER: str
RESOURCE_SLA_MISS: str
RESOURCE_TASK_INSTANCE: str
RESOURCE_TASK_RESCHEDULE: str
RESOURCE_TRIGGER: str
RESOURCE_VARIABLE: str
RESOURCE_XCOM: str
NEW_SESSION: None
EXISTING_ROLES: set

class AirflowSecurityManagerV2(airflow.utils.log.logging_mixin.LoggingMixin):
    _auth_manager_is_authorized_map: ClassVar[functools.cached_property] = ...
    def __init__(self, appbuilder) -> None: ...
    @staticmethod
    def before_request(): ...
    def create_limiter(self) -> Limiter: ...
    def register_views(self): ...
    def has_access(self, action_name: str, resource_name: str, user: Incomplete | None = ..., resource_pk: str | None = ...) -> bool: ...
    def create_admin_standalone(self) -> tuple[str | None, str | None]: ...
    def add_limit_view(self, baseview): ...
    def get_action(self, name: str) -> Action: ...
    def get_resource(self, name: str) -> Resource: ...
    def add_permissions_view(self, base_action_names, resource_name): ...
    def add_permissions_menu(self, resource_name): ...
