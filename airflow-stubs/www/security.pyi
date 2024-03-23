import airflow.auth.managers.fab.security_manager.override
from airflow.auth.managers.fab.security_manager.override import FabAirflowSecurityManagerOverride as FabAirflowSecurityManagerOverride

EXISTING_ROLES: set

class AirflowSecurityManager(airflow.auth.managers.fab.security_manager.override.FabAirflowSecurityManagerOverride):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
