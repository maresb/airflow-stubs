from airflow.exceptions import AirflowTimetableInvalid as AirflowTimetableInvalid
from airflow.utils.dates import cron_presets as cron_presets
from airflow.utils.timezone import convert_to_utc as convert_to_utc, make_aware as make_aware, make_naive as make_naive, parse_timezone as parse_timezone
from pendulum import DateTime as DateTime
from pendulum.tz.timezone import FixedTimezone as FixedTimezone, Timezone as Timezone
from typing import Any

class CronMixin:
    description: str
    def __init__(self, cron: str, timezone: str | Timezone | FixedTimezone) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @property
    def summary(self) -> str: ...
    def validate(self) -> None: ...
