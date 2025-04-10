import attrs
from airflow.datasets import Dataset as Dataset, DatasetAlias as DatasetAlias, extract_event_key as extract_event_key
from typing import Any

@attrs.define(init=False)
class Metadata:
    uri: str
    extra: dict[str, Any]
    alias_name: str | None = ...
