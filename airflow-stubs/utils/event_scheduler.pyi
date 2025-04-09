from _typeshed import Incomplete
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from sched import scheduler
from typing import Callable

class EventScheduler(scheduler, LoggingMixin):
    def call_regular_interval(self, delay: float, action: Callable, arguments=(), kwargs: Incomplete | None = None): ...
