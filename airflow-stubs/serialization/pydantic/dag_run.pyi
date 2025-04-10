from _typeshed import Incomplete
from airflow.jobs.scheduler_job_runner import TI as TI
from airflow.models.dagrun import DagRun as DagRun
from airflow.serialization.pydantic.dag import PydanticDag as PydanticDag
from airflow.serialization.pydantic.dataset import DatasetEventPydantic as DatasetEventPydantic
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.utils.pydantic import BaseModel as BaseModelPydantic, ConfigDict as ConfigDict, is_pydantic_2_installed as is_pydantic_2_installed
from airflow.utils.state import TaskInstanceState as TaskInstanceState
from datetime import datetime
from sqlalchemy.orm import Session as Session
from typing import Iterable

class DagRunPydantic(BaseModelPydantic):
    id: int
    dag_id: str
    queued_at: datetime | None
    execution_date: datetime
    start_date: datetime | None
    end_date: datetime | None
    state: str
    run_id: str
    creating_job_id: int | None
    external_trigger: bool
    run_type: str
    conf: dict
    data_interval_start: datetime | None
    data_interval_end: datetime | None
    last_scheduling_decision: datetime | None
    dag_hash: str | None
    updated_at: datetime | None
    dag: PydanticDag | None
    consumed_dataset_events: list[DatasetEventPydantic]
    log_template_id: int | None
    model_config: Incomplete
    @property
    def logical_date(self) -> datetime: ...
    def get_task_instances(self, state: Iterable[TaskInstanceState | None] | None = None, session: Incomplete | None = None) -> list[TI]: ...
    def get_task_instance(self, task_id: str, session: Session, *, map_index: int = -1) -> TI | TaskInstancePydantic | None: ...
    def get_log_template(self, session: Session): ...
