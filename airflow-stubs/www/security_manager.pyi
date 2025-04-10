from _typeshed import Incomplete
from airflow.auth.managers.models.base_user import BaseUser as BaseUser
from airflow.auth.managers.models.resource_details import AccessView as AccessView, ConnectionDetails as ConnectionDetails, DagAccessEntity as DagAccessEntity, DagDetails as DagDetails, PoolDetails as PoolDetails, VariableDetails as VariableDetails
from airflow.auth.managers.utils.fab import get_method_from_fab_action_map as get_method_from_fab_action_map
from airflow.exceptions import AirflowException as AirflowException
from airflow.models import Connection as Connection, DagRun as DagRun, Pool as Pool, TaskInstance as TaskInstance, Variable as Variable
from airflow.security.permissions import RESOURCE_ADMIN_MENU as RESOURCE_ADMIN_MENU, RESOURCE_AUDIT_LOG as RESOURCE_AUDIT_LOG, RESOURCE_BROWSE_MENU as RESOURCE_BROWSE_MENU, RESOURCE_CLUSTER_ACTIVITY as RESOURCE_CLUSTER_ACTIVITY, RESOURCE_CONFIG as RESOURCE_CONFIG, RESOURCE_CONNECTION as RESOURCE_CONNECTION, RESOURCE_DAG as RESOURCE_DAG, RESOURCE_DAG_CODE as RESOURCE_DAG_CODE, RESOURCE_DAG_DEPENDENCIES as RESOURCE_DAG_DEPENDENCIES, RESOURCE_DAG_RUN as RESOURCE_DAG_RUN, RESOURCE_DATASET as RESOURCE_DATASET, RESOURCE_DOCS as RESOURCE_DOCS, RESOURCE_DOCS_MENU as RESOURCE_DOCS_MENU, RESOURCE_JOB as RESOURCE_JOB, RESOURCE_PLUGIN as RESOURCE_PLUGIN, RESOURCE_POOL as RESOURCE_POOL, RESOURCE_PROVIDER as RESOURCE_PROVIDER, RESOURCE_SLA_MISS as RESOURCE_SLA_MISS, RESOURCE_TASK_INSTANCE as RESOURCE_TASK_INSTANCE, RESOURCE_TASK_RESCHEDULE as RESOURCE_TASK_RESCHEDULE, RESOURCE_TRIGGER as RESOURCE_TRIGGER, RESOURCE_VARIABLE as RESOURCE_VARIABLE, RESOURCE_XCOM as RESOURCE_XCOM
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from airflow.www.utils import CustomSQLAInterface as CustomSQLAInterface
from flask_limiter import Limiter
from functools import cached_property as cached_property

EXISTING_ROLES: Incomplete

class AirflowSecurityManagerV2(LoggingMixin):
    appbuilder: Incomplete
    limiter: Incomplete
    def __init__(self, appbuilder) -> None: ...
    @staticmethod
    def before_request() -> None: ...
    def create_limiter(self) -> Limiter: ...
    def register_views(self) -> None: ...
    def has_access(self, action_name: str, resource_name: str, user: Incomplete | None = None, resource_pk: str | None = None) -> bool: ...
    def create_admin_standalone(self) -> tuple[str | None, str | None]: ...
    def add_limit_view(self, baseview) -> None: ...
    def add_permissions_view(self, base_action_names, resource_name) -> None: ...
    def add_permissions_menu(self, resource_name) -> None: ...
