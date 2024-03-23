from airflow.configuration import conf as conf
from airflow.exceptions import AirflowConfigException as AirflowConfigException
from airflow.utils.module_loading import import_string as import_string

TYPE_CHECKING: bool
STANDARD_TASK_RUNNER: str
CGROUP_TASK_RUNNER: str
CORE_TASK_RUNNERS: dict
def get_task_runner(local_task_job_runner: LocalTaskJobRunner) -> BaseTaskRunner: ...
