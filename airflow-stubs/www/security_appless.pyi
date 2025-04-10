from _typeshed import Incomplete
from airflow.providers.fab.auth_manager.security_manager.override import FabAirflowSecurityManagerOverride as FabAirflowSecurityManagerOverride
from flask_session import Session as Session

class FakeAppBuilder:
    get_session: Incomplete
    def __init__(self, session: Session | None = None) -> None: ...

class ApplessAirflowSecurityManager(FabAirflowSecurityManagerOverride):
    appbuilder: Incomplete
    def __init__(self, session: Session | None = None) -> None: ...
