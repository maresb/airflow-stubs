from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from airflow.models import TaskInstance as TaskInstance

def get_task(dag_id: str, task_id: str) -> TaskInstance: ...
