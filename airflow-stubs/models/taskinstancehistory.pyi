from _typeshed import Incomplete
from airflow.models.base import Base as Base, StringID as StringID
from airflow.models.taskinstance import TaskInstance as TaskInstance
from airflow.serialization.pydantic.taskinstance import TaskInstancePydantic as TaskInstancePydantic
from airflow.utils import timezone as timezone
from airflow.utils.session import NEW_SESSION as NEW_SESSION, provide_session as provide_session
from airflow.utils.sqlalchemy import ExecutorConfigType as ExecutorConfigType, ExtendedJSON as ExtendedJSON, UtcDateTime as UtcDateTime
from airflow.utils.state import State as State, TaskInstanceState as TaskInstanceState

class TaskInstanceHistory(Base):
    __tablename__: str
    id: Incomplete
    task_id: Incomplete
    dag_id: Incomplete
    run_id: Incomplete
    map_index: Incomplete
    try_number: Incomplete
    start_date: Incomplete
    end_date: Incomplete
    duration: Incomplete
    state: Incomplete
    max_tries: Incomplete
    hostname: Incomplete
    unixname: Incomplete
    job_id: Incomplete
    pool: Incomplete
    pool_slots: Incomplete
    queue: Incomplete
    priority_weight: Incomplete
    operator: Incomplete
    custom_operator_name: Incomplete
    queued_dttm: Incomplete
    queued_by_job_id: Incomplete
    pid: Incomplete
    executor: Incomplete
    executor_config: Incomplete
    updated_at: Incomplete
    rendered_map_index: Incomplete
    external_executor_id: Incomplete
    trigger_id: Incomplete
    trigger_timeout: Incomplete
    next_method: Incomplete
    next_kwargs: Incomplete
    task_display_name: Incomplete
    def __init__(self, ti: TaskInstance | TaskInstancePydantic, state: str | None = None) -> None: ...
    __table_args__: Incomplete
    @staticmethod
    def record_ti(ti: TaskInstance, session: NEW_SESSION = None) -> None: ...
