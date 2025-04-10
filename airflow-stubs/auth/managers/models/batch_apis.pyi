from airflow.auth.managers.base_auth_manager import ResourceMethod as ResourceMethod
from airflow.auth.managers.models.resource_details import ConnectionDetails as ConnectionDetails, DagAccessEntity as DagAccessEntity, DagDetails as DagDetails, PoolDetails as PoolDetails, VariableDetails as VariableDetails
from typing import TypedDict

class IsAuthorizedConnectionRequest(TypedDict, total=False):
    method: ResourceMethod
    details: ConnectionDetails | None

class IsAuthorizedDagRequest(TypedDict, total=False):
    method: ResourceMethod
    access_entity: DagAccessEntity | None
    details: DagDetails | None

class IsAuthorizedPoolRequest(TypedDict, total=False):
    method: ResourceMethod
    details: PoolDetails | None

class IsAuthorizedVariableRequest(TypedDict, total=False):
    method: ResourceMethod
    details: VariableDetails | None
