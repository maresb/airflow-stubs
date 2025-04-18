from _typeshed import Incomplete
from airflow.executors.executor_constants import CORE_EXECUTOR_NAMES as CORE_EXECUTOR_NAMES, ConnectorSource as ConnectorSource
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin

class ExecutorName(LoggingMixin):
    module_path: Incomplete
    alias: Incomplete
    def __init__(self, module_path, alias: Incomplete | None = None) -> None: ...
    connector_source: Incomplete
    def set_connector_source(self) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
