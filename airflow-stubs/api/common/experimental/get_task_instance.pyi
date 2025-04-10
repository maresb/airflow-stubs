from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag, check_and_get_dagrun as check_and_get_dagrun
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning, TaskInstanceNotFound as TaskInstanceNotFound
from airflow.models import TaskInstance as TaskInstance
from datetime import datetime

def get_task_instance(dag_id: str, task_id: str, execution_date: datetime) -> TaskInstance: ...
