from airflow.models import DAG as DAG, DagRun as DagRun
from airflow.operators.branch import BaseBranchOperator as BaseBranchOperator
from airflow.utils.context import Context as Context
from typing import Iterable

class LatestOnlyOperator(BaseBranchOperator):
    ui_color: str
    def choose_branch(self, context: Context) -> str | Iterable[str]: ...
