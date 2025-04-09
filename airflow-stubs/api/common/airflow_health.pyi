from airflow.jobs.dag_processor_job_runner import DagProcessorJobRunner as DagProcessorJobRunner
from airflow.jobs.scheduler_job_runner import SchedulerJobRunner as SchedulerJobRunner
from airflow.jobs.triggerer_job_runner import TriggererJobRunner as TriggererJobRunner
from typing import Any

HEALTHY: str
UNHEALTHY: str

def get_airflow_health() -> dict[str, Any]: ...
