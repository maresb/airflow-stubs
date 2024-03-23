from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag, check_and_get_dagrun as check_and_get_dagrun
from airflow.exceptions import TaskInstanceNotFound as TaskInstanceNotFound
from airflow.models.taskinstance import TaskInstance as TaskInstance

TYPE_CHECKING: bool
def get_task_instance(dag_id: str, task_id: str, execution_date: datetime) -> TaskInstance: ...
