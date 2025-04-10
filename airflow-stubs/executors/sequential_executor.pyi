from _typeshed import Incomplete
from airflow.executors.base_executor import BaseExecutor as BaseExecutor, CommandType as CommandType
from airflow.models.taskinstancekey import TaskInstanceKey as TaskInstanceKey
from airflow.traces.tracer import Trace as Trace, span as span
from typing import Any

class SequentialExecutor(BaseExecutor):
    supports_pickling: bool
    is_local: bool
    is_single_threaded: bool
    is_production: bool
    serve_logs: bool
    commands_to_run: Incomplete
    def __init__(self) -> None: ...
    def execute_async(self, key: TaskInstanceKey, command: CommandType, queue: str | None = None, executor_config: Any | None = None) -> None: ...
    def sync(self) -> None: ...
    def end(self) -> None: ...
    def terminate(self) -> None: ...
