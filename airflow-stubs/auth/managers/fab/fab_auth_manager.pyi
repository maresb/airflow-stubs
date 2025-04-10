from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.providers.fab.auth_manager.fab_auth_manager import FabAuthManager as FabAuthManagerProvider

class FabAuthManager(FabAuthManagerProvider): ...
