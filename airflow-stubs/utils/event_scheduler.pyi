import airflow.utils.log.logging_mixin
import sched
from _typeshed import Incomplete
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Callable

class EventScheduler(sched.scheduler, airflow.utils.log.logging_mixin.LoggingMixin):
    def call_regular_interval(self, delay: float, action: Callable, arguments: tuple = ..., kwargs: Incomplete | None = ...): ...
