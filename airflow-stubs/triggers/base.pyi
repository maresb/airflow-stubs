import abc
from _typeshed import Incomplete
from airflow.callbacks.callback_requests import TaskCallbackRequest as TaskCallbackRequest
from airflow.callbacks.database_callback_sink import DatabaseCallbackSink as DatabaseCallbackSink
from airflow.models import TaskInstance as TaskInstance
from airflow.models.taskinstance import SimpleTaskInstance as SimpleTaskInstance
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from dataclasses import dataclass
from datetime import timedelta
from sqlalchemy.orm import Session as Session
from typing import Any, AsyncIterator

log: Incomplete

@dataclass
class StartTriggerArgs:
    trigger_cls: str
    next_method: str
    trigger_kwargs: dict[str, Any] | None = ...
    next_kwargs: dict[str, Any] | None = ...
    timeout: timedelta | None = ...

class BaseTrigger(abc.ABC, LoggingMixin, metaclass=abc.ABCMeta):
    task_instance: Incomplete
    trigger_id: Incomplete
    def __init__(self, **kwargs) -> None: ...
    @abc.abstractmethod
    def serialize(self) -> tuple[str, dict[str, Any]]: ...
    @abc.abstractmethod
    async def run(self) -> AsyncIterator[TriggerEvent]: ...
    async def cleanup(self) -> None: ...

class TriggerEvent:
    payload: Incomplete
    def __init__(self, payload: Any) -> None: ...
    def __eq__(self, other): ...
    def handle_submit(self, *, task_instance: TaskInstance, session: Session = ...) -> None: ...

class BaseTaskEndEvent(TriggerEvent):
    task_instance_state: TaskInstanceState
    xcoms: Incomplete
    def __init__(self, *, xcoms: dict[str, Any] | None = None, **kwargs) -> None: ...
    def handle_submit(self, *, task_instance: TaskInstance, session: Session = ...) -> None: ...

class TaskSuccessEvent(BaseTaskEndEvent):
    task_instance_state: Incomplete

class TaskFailedEvent(BaseTaskEndEvent):
    task_instance_state: Incomplete

class TaskSkippedEvent(BaseTaskEndEvent):
    task_instance_state: Incomplete
