import airflow.utils.log.timezone_aware
import colorlog.colorlog
from airflow.utils.log.timezone_aware import TimezoneAware as TimezoneAware

TYPE_CHECKING: bool
escape_codes: dict
DEFAULT_COLORS: dict
BOLD_ON: str
BOLD_OFF: str

class CustomTTYColoredFormatter(colorlog.colorlog.TTYColoredFormatter, airflow.utils.log.timezone_aware.TimezoneAware):
    def __init__(self, *args, **kwargs) -> None: ...
    def format(self, record: LogRecord) -> str: ...
