import logging
from _typeshed import Incomplete
from airflow.utils import timezone as timezone

class TimezoneAware(logging.Formatter):
    default_time_format: str
    default_msec_format: str
    default_tz_format: str
    def formatTime(self, record, datefmt: Incomplete | None = None): ...
