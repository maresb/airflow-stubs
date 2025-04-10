import datetime
from _typeshed import Incomplete
from airflow.api_internal.internal_api_call import internal_api_call as internal_api_call
from airflow.models.base import Base as Base
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.serialization.pydantic.trigger import TriggerPydantic as TriggerPydantic
from airflow.triggers.base import BaseTrigger as BaseTrigger
from airflow.utils import timezone as timezone
from airflow.utils.retries import run_with_db_retries as run_with_db_retries
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import UtcDateTime as UtcDateTime, with_row_locks as with_row_locks
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from sqlalchemy.orm import Session as Session
from sqlalchemy.sql import Select as Select
from typing import Any, Iterable

class Trigger(Base):
    __tablename__: str
    id: Incomplete
    classpath: Incomplete
    encrypted_kwargs: Incomplete
    created_date: Incomplete
    triggerer_id: Incomplete
    triggerer_job: Incomplete
    task_instance: Incomplete
    def __init__(self, classpath: str, kwargs: dict[str, Any], created_date: datetime.datetime | None = None) -> None: ...
    @property
    def kwargs(self) -> dict[str, Any]: ...
    @kwargs.setter
    def kwargs(self, kwargs: dict[str, Any]) -> None: ...
    def rotate_fernet_key(self) -> None: ...
    @classmethod
    def from_object(cls, trigger: BaseTrigger, session=...) -> Trigger | TriggerPydantic: ...
    @classmethod
    def bulk_fetch(cls, ids: Iterable[int], session: Session = ...) -> dict[int, Trigger]: ...
    @classmethod
    def clean_unused(cls, session: Session = ...) -> None: ...
    @classmethod
    def submit_event(cls, trigger_id, event, session: Session = ...) -> None: ...
    @classmethod
    def submit_failure(cls, trigger_id, exc: Incomplete | None = None, session: Session = ...) -> None: ...
    @classmethod
    def ids_for_triggerer(cls, triggerer_id, session: Session = ...) -> list[int]: ...
    @classmethod
    def assign_unassigned(cls, triggerer_id, capacity, health_check_threshold, session: Session = ...) -> None: ...
    @classmethod
    def get_sorted_triggers(cls, capacity: int, alive_triggerer_ids: list[int] | Select, session: Session): ...
