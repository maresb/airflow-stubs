import airflow.jobs.base_job_runner
import airflow.utils.log.logging_mixin
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import Job as Job, perform_heartbeat as perform_heartbeat
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any, ClassVar

TYPE_CHECKING: bool
def empty_callback(_: Any) -> None: ...

class DagProcessorJobRunner(airflow.jobs.base_job_runner.BaseJobRunner, airflow.utils.log.logging_mixin.LoggingMixin):
    job_type: ClassVar[str] = ...
    def __init__(self, job: Job, processor: DagFileProcessorManager, *args, **kwargs) -> None: ...
