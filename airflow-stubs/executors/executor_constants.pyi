from _typeshed import Incomplete
from enum import Enum

class ConnectorSource(Enum):
    CORE = 'core'
    PLUGIN = 'plugin'
    CUSTOM_PATH = 'custom path'

LOCAL_EXECUTOR: str
LOCAL_KUBERNETES_EXECUTOR: str
SEQUENTIAL_EXECUTOR: str
CELERY_EXECUTOR: str
CELERY_KUBERNETES_EXECUTOR: str
KUBERNETES_EXECUTOR: str
DEBUG_EXECUTOR: str
MOCK_EXECUTOR: str
CORE_EXECUTOR_NAMES: Incomplete
