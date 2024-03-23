from airflow.api.common.experimental import check_and_get_dag as check_and_get_dag
from airflow.models.dagrun import DagRun as DagRun
from airflow.utils.state import DagRunState as DagRunState
from typing import Any

def get_dag_runs(dag_id: str, state: str | None = ...) -> list[dict[str, Any]]: ...
