import airflow.utils.timezone as timezone
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from typing import Collection
from typing_extensions import TimeUnit

cron_presets: dict
def date_range(start_date: datetime, end_date: datetime | None = ..., num: int | None = ..., delta: str | timedelta | relativedelta | None = ...) -> list[datetime]: ...
def round_time(dt: datetime, delta: str | timedelta | relativedelta, start_date: datetime = ...): ...
def infer_time_unit(time_seconds_arr: Collection[float]) -> TimeUnit: ...
def scale_time_units(time_seconds_arr: Collection[float], unit: TimeUnit) -> Collection[float]: ...
def days_ago(n, hour: int = ..., minute: int = ..., second: int = ..., microsecond: int = ...): ...
def parse_execution_date(execution_date_str): ...