from airflow.utils.deprecation_tools import add_deprecated_classes as add_deprecated_classes
from babel import Locale
from pendulum import DateTime as DateTime
from random import random as random
from typing import Any

def ds_add(ds: str, days: int) -> str: ...
def ds_format(ds: str, input_format: str, output_format: str) -> str: ...
def ds_format_locale(ds: str, input_format: str, output_format: str, locale: Locale | str | None = None) -> str: ...
def datetime_diff_for_humans(dt: Any, since: DateTime | None = None) -> str: ...
