import datetime
import pendulum
from _typeshed import Incomplete
from airflow.triggers.base import BaseTrigger as BaseTrigger, TaskSuccessEvent as TaskSuccessEvent, TriggerEvent as TriggerEvent
from airflow.utils import timezone as timezone
from typing import Any, AsyncIterator

class DateTimeTrigger(BaseTrigger):
    moment: pendulum.DateTime
    end_from_trigger: Incomplete
    def __init__(self, moment: datetime.datetime, *, end_from_trigger: bool = False) -> None: ...
    def serialize(self) -> tuple[str, dict[str, Any]]: ...
    async def run(self) -> AsyncIterator[TriggerEvent]: ...

class TimeDeltaTrigger(DateTimeTrigger):
    def __init__(self, delta: datetime.timedelta, *, end_from_trigger: bool = False) -> None: ...
