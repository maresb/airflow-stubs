from _typeshed import Incomplete
from airflow.dag_processing.manager import DagFileProcessorManager as DagFileProcessorManager
from airflow.jobs.base_job_runner import BaseJobRunner as BaseJobRunner
from airflow.jobs.job import Job as Job, perform_heartbeat as perform_heartbeat
from airflow.utils.log.logging_mixin import LoggingMixin as LoggingMixin
from typing import Any

def empty_callback(_: Any) -> None: ...

class DagProcessorJobRunner(BaseJobRunner, LoggingMixin):
    job_type: str
    processor: Incomplete
    def __init__(self, job: Job, processor: DagFileProcessorManager, *args, **kwargs) -> None: ...
