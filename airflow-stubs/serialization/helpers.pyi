from airflow.configuration import conf as conf
from airflow.settings import json as json
from airflow.utils.log.secrets_masker import redact as redact
from typing import Any

def serialize_template_field(template_field: Any, name: str) -> str | dict | list | int | float: ...
