from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag

TYPE_CHECKING: bool
def get_task(dag_id: str, task_id: str) -> TaskInstance: ...
