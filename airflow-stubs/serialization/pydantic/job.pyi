import datetime
from _typeshed import Incomplete
from airflow.executors.executor_loader import ExecutorLoader as ExecutorLoader
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.utils.pydantic import BaseModel as BaseModelPydantic, ConfigDict as ConfigDict
from functools import cached_property as cached_property

def check_runner_initialized(job_runner: BaseJobRunner | None, job_type: str) -> BaseJobRunner: ...

class JobPydantic(BaseModelPydantic):
    id: int | None
    dag_id: str | None
    state: str | None
    job_type: str | None
    start_date: datetime.datetime | None
    end_date: datetime.datetime | None
    latest_heartbeat: datetime.datetime
    executor_class: str | None
    hostname: str | None
    unixname: str | None
    grace_multiplier: float
    model_config: Incomplete
    @cached_property
    def executor(self): ...
    @cached_property
    def heartrate(self) -> float: ...
    def is_alive(self) -> bool: ...
