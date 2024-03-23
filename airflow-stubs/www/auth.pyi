import typing
from airflow.auth.managers.models.resource_details import AccessView as AccessView, ConnectionDetails as ConnectionDetails, DagAccessEntity as DagAccessEntity, DagDetails as DagDetails, PoolDetails as PoolDetails, VariableDetails as VariableDetails
from airflow.configuration import conf as conf
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.utils.net import get_hostname as get_hostname
from airflow.www.extensions.init_auth_manager import get_auth_manager as get_auth_manager
from typing import Callable, Sequence

TYPE_CHECKING: bool
LOGMSG_ERR_SEC_ACCESS_DENIED: str
PERMISSION_PREFIX: str
T: typing.TypeVar
def get_access_denied_message(): ...
def has_access(permissions: Sequence[tuple[str, str]] | None = ...) -> Callable[[T], T]: ...
def has_access_with_pk(f): ...
def has_access_cluster_activity(method: ResourceMethod) -> Callable[[T], T]: ...
def has_access_configuration(method: ResourceMethod) -> Callable[[T], T]: ...
def has_access_connection(method: ResourceMethod) -> Callable[[T], T]: ...
def has_access_dag(method: ResourceMethod, access_entity: DagAccessEntity | None = ...) -> Callable[[T], T]: ...
def has_access_dag_entities(method: ResourceMethod, access_entity: DagAccessEntity) -> Callable[[T], T]: ...
def has_access_dataset(method: ResourceMethod) -> Callable[[T], T]: ...
def has_access_pool(method: ResourceMethod) -> Callable[[T], T]: ...
def has_access_variable(method: ResourceMethod) -> Callable[[T], T]: ...
def has_access_view(access_view: AccessView = ...) -> Callable[[T], T]: ...
