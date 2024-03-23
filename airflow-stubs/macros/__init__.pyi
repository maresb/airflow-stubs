import airflow.utils.yaml as yaml
from airflow.utils.deprecation_tools import add_deprecated_classes as add_deprecated_classes
from typing import Any

random: builtin_function_or_method
TYPE_CHECKING: bool
def ds_add(ds: str, days: int) -> str: ...
def ds_format(ds: str, input_format: str, output_format: str) -> str: ...
def datetime_diff_for_humans(dt: Any, since: DateTime | None = ...) -> str: ...