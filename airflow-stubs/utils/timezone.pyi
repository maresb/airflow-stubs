import datetime as dt
from _typeshed import Incomplete
from airflow.typing_compat import Literal as Literal
from pendulum.datetime import DateTime
from pendulum.tz.timezone import FixedTimezone as FixedTimezone, Timezone as Timezone
from typing import overload

utc: Incomplete

def is_localized(value): ...
def is_naive(value): ...
def utcnow() -> dt.datetime: ...
def utc_epoch() -> dt.datetime: ...
@overload
def convert_to_utc(value: None) -> None: ...
@overload
def convert_to_utc(value: dt.datetime) -> DateTime: ...
@overload
def make_aware(value: None, timezone: dt.tzinfo | None = None) -> None: ...
@overload
def make_aware(value: DateTime, timezone: dt.tzinfo | None = None) -> DateTime: ...
@overload
def make_aware(value: dt.datetime, timezone: dt.tzinfo | None = None) -> dt.datetime: ...
def make_naive(value, timezone: Incomplete | None = None): ...
def datetime(*args, **kwargs): ...
def parse(string: str, timezone: Incomplete | None = None, *, strict: bool = False) -> DateTime: ...
@overload
def coerce_datetime(v: None, tz: dt.tzinfo | None = None) -> None: ...
@overload
def coerce_datetime(v: DateTime, tz: dt.tzinfo | None = None) -> DateTime: ...
@overload
def coerce_datetime(v: dt.datetime, tz: dt.tzinfo | None = None) -> DateTime: ...
def td_format(td_object: None | dt.timedelta | float | int) -> str | None: ...
def parse_timezone(name: str | int) -> FixedTimezone | Timezone: ...
def local_timezone() -> FixedTimezone | Timezone: ...
def from_timestamp(timestamp: int | float, tz: str | FixedTimezone | Timezone | Literal['local'] = ...) -> DateTime: ...
