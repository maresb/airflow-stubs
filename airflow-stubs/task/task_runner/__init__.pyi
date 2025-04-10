from _typeshed import Incomplete
from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.jobs.local_task_job_runner import LocalTaskJobRunner as LocalTaskJobRunner
from airflow.task.task_runner.base_task_runner import BaseTaskRunner as BaseTaskRunner
from airflow.utils.module_loading import import_string as import_string

log: Incomplete
STANDARD_TASK_RUNNER: str
CGROUP_TASK_RUNNER: str
CORE_TASK_RUNNERS: Incomplete

def get_task_runner(local_task_job_runner: LocalTaskJobRunner) -> BaseTaskRunner: ...
