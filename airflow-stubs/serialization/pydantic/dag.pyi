import pathlib
from _typeshed import Incomplete
from airflow import DAG as DAG, settings as settings
from airflow.utils.pydantic import BaseModel as BaseModelPydantic, ConfigDict as ConfigDict, PlainSerializer as PlainSerializer, PlainValidator as PlainValidator, ValidationInfo as ValidationInfo
from airflow.utils.sqlalchemy import Interval as Interval
from datetime import datetime
from typing import Any

def serialize_interval(value: Interval) -> Interval: ...
def validate_interval(value: Interval | Any, _info: ValidationInfo) -> Any: ...

PydanticInterval: Incomplete

def serialize_operator(x: DAG) -> dict: ...
def validate_operator(x: DAG | dict[str, Any], _info: ValidationInfo) -> Any: ...

PydanticDag: Incomplete

class DagOwnerAttributesPydantic(BaseModelPydantic):
    owner: str
    link: str
    model_config: Incomplete

class DagTagPydantic(BaseModelPydantic):
    name: str
    dag_id: str
    model_config: Incomplete

class DagModelPydantic(BaseModelPydantic):
    dag_id: str
    root_dag_id: str | None
    is_paused_at_creation: bool
    is_paused: bool
    is_subdag: bool | None
    is_active: bool | None
    last_parsed_time: datetime | None
    last_pickled: datetime | None
    last_expired: datetime | None
    scheduler_lock: bool | None
    pickle_id: int | None
    fileloc: str
    processor_subdir: str | None
    owners: str | None
    description: str | None
    default_view: str | None
    schedule_interval: PydanticInterval | None
    timetable_description: str | None
    tags: list[DagTagPydantic]
    dag_owner_links: list[DagOwnerAttributesPydantic]
    parent_dag: PydanticDag | None
    max_active_tasks: int
    max_active_runs: int | None
    max_consecutive_failed_dag_runs: int | None
    has_task_concurrency_limits: bool
    has_import_errors: bool | None
    model_config: Incomplete
    @property
    def relative_fileloc(self) -> pathlib.Path: ...
