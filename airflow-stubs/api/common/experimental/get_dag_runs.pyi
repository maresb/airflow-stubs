from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag
from airflow.models import DagRun as DagRun
from airflow.utils.state import DagRunState as DagRunState
from typing import Any

def get_dag_runs(dag_id: str, state: str | None = None) -> list[dict[str, Any]]: ...
