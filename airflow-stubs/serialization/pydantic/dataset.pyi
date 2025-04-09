from _typeshed import Incomplete
from airflow.utils.pydantic import BaseModel as BaseModelPydantic, ConfigDict as ConfigDict
from datetime import datetime

class DagScheduleDatasetReferencePydantic(BaseModelPydantic):
    dataset_id: int
    dag_id: str
    created_at: datetime
    updated_at: datetime
    model_config: Incomplete

class TaskOutletDatasetReferencePydantic(BaseModelPydantic):
    dataset_id: int
    dag_id: str
    task_id: str
    created_at: datetime
    updated_at: datetime
    model_config: Incomplete

class DatasetPydantic(BaseModelPydantic):
    id: int
    uri: str
    extra: dict | None
    created_at: datetime
    updated_at: datetime
    is_orphaned: bool
    consuming_dags: list[DagScheduleDatasetReferencePydantic]
    producing_tasks: list[TaskOutletDatasetReferencePydantic]
    model_config: Incomplete

class DatasetEventPydantic(BaseModelPydantic):
    id: int
    dataset_id: int | None
    extra: dict
    source_task_id: str | None
    source_dag_id: str | None
    source_run_id: str | None
    source_map_index: int | None
    timestamp: datetime
    dataset: DatasetPydantic | None
    model_config: Incomplete
