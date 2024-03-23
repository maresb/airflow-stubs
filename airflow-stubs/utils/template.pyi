from airflow.template.templater import LiteralValue as LiteralValue
from typing import Any

def literal(value: Any) -> LiteralValue: ...
