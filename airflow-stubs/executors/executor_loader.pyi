from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import InternalApiConfig as InternalApiConfig
from airflow.exceptions import AirflowConfigException as AirflowConfigException, UnknownExecutorException as UnknownExecutorException
from airflow.executors.base_executor import BaseExecutor as BaseExecutor
from airflow.executors.executor_constants import CELERY_EXECUTOR as CELERY_EXECUTOR, CELERY_KUBERNETES_EXECUTOR as CELERY_KUBERNETES_EXECUTOR, CORE_EXECUTOR_NAMES as CORE_EXECUTOR_NAMES, ConnectorSource as ConnectorSource, DEBUG_EXECUTOR as DEBUG_EXECUTOR, KUBERNETES_EXECUTOR as KUBERNETES_EXECUTOR, LOCAL_EXECUTOR as LOCAL_EXECUTOR, LOCAL_KUBERNETES_EXECUTOR as LOCAL_KUBERNETES_EXECUTOR, SEQUENTIAL_EXECUTOR as SEQUENTIAL_EXECUTOR
from airflow.executors.executor_utils import ExecutorName as ExecutorName
from airflow.utils.module_loading import import_string as import_string

log: Incomplete

class ExecutorLoader:
    executors: Incomplete
    @classmethod
    def get_executor_names(cls) -> list[ExecutorName]: ...
    @classmethod
    def get_default_executor_name(cls) -> ExecutorName: ...
    @classmethod
    def get_default_executor(cls) -> BaseExecutor: ...
    @classmethod
    def set_default_executor(cls, executor: BaseExecutor) -> None: ...
    @classmethod
    def init_executors(cls) -> list[BaseExecutor]: ...
    @classmethod
    def lookup_executor_name_by_str(cls, executor_name_str: str) -> ExecutorName: ...
    @classmethod
    def load_executor(cls, executor_name: ExecutorName | str | None) -> BaseExecutor: ...
    @classmethod
    def import_executor_cls(cls, executor_name: ExecutorName, validate: bool = True) -> tuple[type[BaseExecutor], ConnectorSource]: ...
    @classmethod
    def import_default_executor_cls(cls, validate: bool = True) -> tuple[type[BaseExecutor], ConnectorSource]: ...
    @classmethod
    def validate_database_executor_compatibility(cls, executor: type[BaseExecutor]) -> None: ...

UNPICKLEABLE_EXECUTORS: Incomplete
