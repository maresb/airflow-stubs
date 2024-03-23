import dt
from _typeshed import Incomplete
from pendulum.datetime import DateTime

TYPE_CHECKING: bool
def is_localized(value): ...
def is_naive(value): ...
def utcnow() -> dt.datetime: ...
def utc_epoch() -> dt.datetime: ...
def convert_to_utc(value: dt.datetime | None) -> DateTime | None: ...
def make_aware(value: dt.datetime | None, timezone: dt.tzinfo | None = ...) -> dt.datetime | None: ...
def make_naive(value, timezone: Incomplete | None = ...): ...
def datetime(*args, **kwargs): ...
def parse(string: str, timezone: Incomplete | None = ...) -> DateTime: ...
def coerce_datetime(v: dt.datetime | None, tz: dt.tzinfo | None = ...) -> DateTime | None: ...
def td_format(td_object: None | dt.timedelta | float | int) -> str | None: ...
def parse_timezone(name: str | int) -> FixedTimezone | Timezone: ...
def local_timezone() -> FixedTimezone | Timezone: ...
def from_timestamp(timestamp: int | float, tz: str | FixedTimezone | Timezone | Literal['local'] = ...) -> DateTime: ...