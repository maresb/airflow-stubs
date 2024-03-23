import airflow.auth.managers.fab.security_manager.override
from airflow.auth.managers.fab.security_manager.override import FabAirflowSecurityManagerOverride as FabAirflowSecurityManagerOverride

TYPE_CHECKING: bool

class FakeAppBuilder:
    def __init__(self, session: Session | None = ...) -> None: ...

class ApplessAirflowSecurityManager(airflow.auth.managers.fab.security_manager.override.FabAirflowSecurityManagerOverride):
    def __init__(self, session: Session | None = ...) -> None: ...
