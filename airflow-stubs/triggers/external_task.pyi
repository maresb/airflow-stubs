import typing
from _typeshed import Incomplete
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models import DagRun as DagRun, TaskInstance as TaskInstance
from airflow.triggers.base import BaseTrigger as BaseTrigger, TriggerEvent as TriggerEvent
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.state import DagRunState as DagRunState, TaskInstanceState as TaskInstanceState
from airflow.utils.timezone import utcnow as utcnow
from datetime import datetime
from sqlalchemy.orm import Session as Session
from typing import Any

class WorkflowTrigger(BaseTrigger):
    external_dag_id: Incomplete
    external_task_ids: Incomplete
    external_task_group_id: Incomplete
    failed_states: Incomplete
    skipped_states: Incomplete
    allowed_states: Incomplete
    execution_dates: Incomplete
    poke_interval: Incomplete
    soft_fail: Incomplete
    def __init__(self, external_dag_id: str, execution_dates: list, external_task_ids: typing.Collection[str] | None = None, external_task_group_id: str | None = None, failed_states: typing.Iterable[str] | None = None, skipped_states: typing.Iterable[str] | None = None, allowed_states: typing.Iterable[str] | None = None, poke_interval: float = 2.0, soft_fail: bool = False, **kwargs) -> None: ...
    def serialize(self) -> tuple[str, dict[str, Any]]: ...
    async def run(self) -> typing.AsyncIterator[TriggerEvent]: ...

class TaskStateTrigger(BaseTrigger):
    dag_id: Incomplete
    task_id: Incomplete
    states: Incomplete
    execution_dates: Incomplete
    poll_interval: Incomplete
    trigger_start_time: Incomplete
    def __init__(self, dag_id: str, execution_dates: list[datetime], trigger_start_time: datetime, states: list[str] | None = None, task_id: str | None = None, poll_interval: float = 2.0) -> None: ...
    def serialize(self) -> tuple[str, dict[str, typing.Any]]: ...
    async def run(self) -> typing.AsyncIterator[TriggerEvent]: ...
    def count_running_dags(self, session: Session): ...
    def count_tasks(self, *, session: Session = ...) -> int | None: ...

class DagStateTrigger(BaseTrigger):
    dag_id: Incomplete
    states: Incomplete
    execution_dates: Incomplete
    poll_interval: Incomplete
    def __init__(self, dag_id: str, states: list[DagRunState], execution_dates: list[datetime], poll_interval: float = 5.0) -> None: ...
    def serialize(self) -> tuple[str, dict[str, typing.Any]]: ...
    async def run(self) -> typing.AsyncIterator[TriggerEvent]: ...
    def count_dags(self, *, session: Session = ...) -> int | None: ...
