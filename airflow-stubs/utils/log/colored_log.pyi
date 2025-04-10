from _typeshed import Incomplete
from airflow.utils.log.timezone_aware import TimezoneAware as TimezoneAware
from colorlog import ColoredFormatter
from logging import LogRecord

DEFAULT_COLORS: Incomplete
BOLD_ON: Incomplete
BOLD_OFF: Incomplete

class CustomTTYColoredFormatter(ColoredFormatter, TimezoneAware):
    def __init__(self, *args, **kwargs) -> None: ...
    def format(self, record: LogRecord) -> str: ...
