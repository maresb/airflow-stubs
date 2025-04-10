from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag, check_and_get_dagrun as check_and_get_dagrun
from airflow.exceptions import RemovedInAirflow3Warning as RemovedInAirflow3Warning
from datetime import datetime

def get_dag_run_state(dag_id: str, execution_date: datetime) -> dict[str, str]: ...
